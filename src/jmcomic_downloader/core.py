import re
import threading
import time
import traceback
from types import TracebackType
from typing import Any

import jmcomic as jm
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
)

from . import text, ui
from .config import cfgs
from .history import history
from .test_domain import test_all_domains

console = Console()


def show_status(arg: bool) -> str:
    return "开启" if arg else "关闭"


class ProgressDownloader(jm.JmDownloader):  # type: ignore[misc]
    """JmDownloader 子类，在日志关闭时用 rich 显示实时下载进度。"""

    def __init__(self, option: Any) -> None:
        super().__init__(option)
        self._progress = Progress(
            TextColumn("{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TextColumn("页"),
            TimeElapsedColumn(),
            transient=True,
        )
        self._task_id: TaskID | None = None
        self._album_pages = 0
        self._lock = threading.Lock()

    def before_album(self, album: jm.JmAlbumDetail) -> None:
        super().before_album(album)
        self._album_pages = 0
        self._progress.start()
        self._task_id = self._progress.add_task(
            f"正在下载: 《{album.name}》",
            total=None,
        )

    def before_photo(self, photo: jm.JmPhotoDetail) -> None:
        super().before_photo(photo)
        # 累加每章的真实页数，实时更新总量
        with self._lock:
            self._album_pages += len(photo)
        if self._task_id is not None:
            self._progress.update(self._task_id, total=self._album_pages)

    def after_image(self, image: jm.JmImageDetail, img_save_path: str) -> None:
        super().after_image(image, img_save_path)
        if self._task_id is not None:
            self._progress.advance(self._task_id)

    def after_album(self, album: jm.JmAlbumDetail) -> None:
        super().after_album(album)
        if self._task_id is not None:
            self._progress.update(self._task_id, completed=self._album_pages)
            self._progress.stop()
        print(f"  ✓ 下载完成 ({self._album_pages}页)")

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self._task_id is not None:
            self._progress.stop()
        super().__exit__(exc_type, exc_val, exc_tb)


def execute_detail(arg: Any) -> dict[str, Any]:
    return {
        "title": arg.name,
        "id": arg.id,
        "author": arg.author,
        "tags": arg.tags,
        "pages": arg.page_count,
        "chapters": len(arg),
    }


def jmcomic_download() -> None:
    jm_ids = ui.input_text("请输入要下载的 JMcomic 车号（多个车号用空格分隔）：")
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return

    # 预获取所有车号的漫画信息
    id_list = jm_ids.split()
    client = jm.JmModuleConfig.option_class().default().build_jm_client()
    album_details: list[Any] = []
    for jm_id in id_list:
        try:
            album = client.get_album_detail(jm_id)
            album_details.append(album)
        except Exception as err:
            print(f"\n**获取车号 {jm_id} 信息时发生错误:")
            print(f"{type(err).__name__}:{err}\n")
            return

    # 使用 rich Panel 展示专辑详情
    for album in album_details:
        authors = ", ".join(str(a) for a in album.authors)
        info_text = (
            f"[bold]标题:[/bold] {album.name}\n"
            f"[bold]作者:[/bold] {authors}\n"
            f"[bold]总页数:[/bold] {album.page_count}\n"
            f"[bold]章节数:[/bold] {len(album)}"
        )
        panel = Panel(
            info_text,
            title=f"📖 漫画信息 — 车号 {album.id}",
            border_style="cyan",
        )
        console.print(panel)

    if ui.confirm("是否开始下载？"):
        downloader_kwargs: dict[str, Any] = (
            {"downloader": ProgressDownloader}
            if not cfgs.show_jm_log
            else {}
        )

        start_time = time.time()
        for jm_id in id_list:
            try:
                album_detail = execute_detail(
                    jm.download_album(jm_id, **downloader_kwargs)[0]
                )
            except Exception as err:
                print("\n**本子不存在或请求时发生错误:")
                print(f"{type(err).__name__}:{err}\n")
            else:
                latest = history.add(album_detail)
                msg = (
                    f"[{latest.get('download_time')}] <{latest.get('jm_id')}> "
                    f"{latest.get('title')} 下载完成！"
                )
                print(msg)
        print(f"所有下载任务已完成，耗时 {time.time() - start_time:.2f} 秒。\n")
    else:
        print("已取消下载任务。")


def setting() -> None:
    while True:
        toggle_label = f"{show_status(not cfgs.show_jm_log)}下载日志输出"
        choices = [text.SETTING_SECTIONS[0], toggle_label] + text.SETTING_SECTIONS[2:]
        command = ui.select(
            message="请选择设置项：",
            choices=choices,
            default=toggle_label,
        )

        if command == toggle_label:
            jm.JmModuleConfig.FLAG_ENABLE_JM_LOG = not jm.JmModuleConfig.FLAG_ENABLE_JM_LOG
            cfgs.show_jm_log = cfgs.edit("show_download_log", jm.JmModuleConfig.FLAG_ENABLE_JM_LOG)
            print(f"已{show_status(cfgs.show_jm_log)}下载日志输出。\n")
        elif command == "测试连接":
            print("正在测试当前IP可访问的Jmcomic域名，请稍候...")
            test_all_domains()
            print("测试完成。\n")
        elif command == "恢复默认":
            if ui.confirm("此操作将重置所有设置且不可逆，确认恢复默认设置？"):
                cfgs.reset()
                print("已恢复默认设置，请重新启动程序以应用更改。\n")
            else:
                print("已取消操作。\n")
        elif command == "切换主题":
            ui.set_style()
        elif command == "设置说明":
            console.print(text.show_settings_panel())
        elif command == "退出设置":
            break
        else:
            print(f'指令 "{command}" 不存在或不可用。')


def execute_command(command: str) -> None:
    if command == "功能说明":
        console.print(text.show_menu_panel())
    elif command == "下载漫画":
        jmcomic_download()
    elif command == "设置选项":
        setting()
    elif command == "历史记录":
        history.print_history()
    elif command == "关于项目":
        console.print(text.show_about_panel())
    elif command == "退出程序":
        print("程序即将退出")
        time.sleep(0.5)
        raise SystemExit(0)
    else:
        print(f'指令"{command}"不存在或不可用。')


def main() -> None:
    cfgs.load()
    history.load()

    choice = "下载漫画"
    console.print(
        Panel(
            "[bold cyan]欢迎使用 JMcomic Downloader！[/bold cyan]",
            border_style="green",
            padding=(1, 2),
        )
    )
    console.print(text.show_menu_panel())
    while True:
        try:
            choice = ui.select(
                message="请选择操作：",
                choices=text.MENU_SECTIONS,
                default=choice,
            )
            execute_command(choice)
        except SystemExit:
            return
        except Exception as err:
            print(f"\n程序发生异常：{type(err).__name__}:{err}\n")
            input("回车以查看详细报错...")
            traceback.print_exc()
