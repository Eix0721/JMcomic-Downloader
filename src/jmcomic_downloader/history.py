import datetime
from typing import Any

import simpsave as ss
from rich.console import Console
from rich.table import Table

from . import ui
from .config import cfgs

console = Console()


class DownloadHistory:
    def __init__(self) -> None:
        self.total_downloads: list[dict[str, Any]] = []
        self._loaded = False

    def load(self) -> None:
        if self._loaded:
            return
        self._loaded = True

        try:
            ss.has("history_exist", file="history.yml")
        except FileNotFoundError:
            print("历史记录文件不存在，正在创建默认历史记录文件...")
            self._reset()
            return
        except Exception as err:
            print(f"读取历史记录文件时发生未知异常：{type(err).__name__}:{err}")

        try:
            print("正在读取历史记录文件...")
            self.total_downloads = ss.read("total_downloads", file="history.yml")
        except FileNotFoundError:
            print("历史记录文件不存在，正在创建默认历史记录文件...")
            self._reset()
        except Exception as err:
            print(f"读取历史记录项时发生错误：{type(err).__name__}:{err}")
            if cfgs.show_jm_log:
                print(f"错误详情：{err}")
            confirm_msg = (
                "您可以将问题反馈给开发者并备份history.yml\n"
                "也可以重置历史记录文件（不推荐），是否重置？"
            )
            if ui.confirm(confirm_msg):
                self._reset()
            else:
                input("请反馈并手动备份history.yml！按回车键退出程序...")
                exit(1)

    def _reset(self) -> None:
        try:
            ss.delete(file="history.yml")
            self.total_downloads = self.edit("total_downloads", [])
        except Exception as err:
            print(f"初始化历史记录文件时发生错误：{type(err).__name__}:{err}")

    def edit(self, key: str, val: Any) -> Any:
        ss.write(key, val, file="history.yml")
        return val

    def save_all(self) -> None:
        try:
            self.edit("total_downloads", self.total_downloads)
        except Exception as err:
            print(f"保存历史记录时发生错误：{type(err).__name__}:{err}")

    def add(self, details: dict[str, Any]) -> dict[str, Any]:
        self.total_downloads.append(
            {
                "jm_id": details.get("id"),
                "title": details.get("title"),
                "author": details.get("author"),
                "download_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
        self.save_all()
        return self.total_downloads[-1]

    def print_history(self) -> None:
        if not self.total_downloads:
            console.print("[yellow]暂无下载记录。[/yellow]")
            return
        table = Table(title="📜 下载历史记录", border_style="cyan")
        table.add_column("序号", style="dim", justify="center")
        table.add_column("车号", style="cyan", justify="center")
        table.add_column("标题", style="green")
        table.add_column("作者", style="yellow")
        table.add_column("下载时间", style="magenta")
        for index, item in enumerate(self.total_downloads):
            table.add_row(
                str(index + 1),
                str(item.get("jm_id", "")),
                str(item.get("title", "")),
                str(item.get("author", "")),
                str(item.get("download_time", "")),
            )
        console.print(table)

    def get_latest(self) -> dict[str, Any] | None:
        return self.total_downloads[-1] if self.total_downloads else None

    def get_recent(self, limit: int = 10) -> list[dict[str, Any]]:
        return self.total_downloads[-limit:] if limit > 0 else self.total_downloads

    def clear_all(self) -> None:
        self.total_downloads = []
        self.save_all()


_history: DownloadHistory | None = None


def get_history() -> DownloadHistory:
    global _history
    if _history is None:
        _history = DownloadHistory()
    return _history


history = get_history()
