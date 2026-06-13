import datetime

import simpsave as ss

from . import ui
from .config import cfgs


class DownloadHistory:
    def __init__(self):
        self.total_downloads: list[dict] = []
        self._loaded = False

    def load(self):
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

    def _reset(self):
        try:
            ss.delete(file="history.yml")
            self.total_downloads = self.edit("total_downloads", [])
        except Exception as err:
            print(f"初始化历史记录文件时发生错误：{type(err).__name__}:{err}")

    def edit(self, key: str, val):
        ss.write(key, val, file="history.yml")
        return val

    def save_all(self):
        try:
            self.edit("total_downloads", self.total_downloads)
        except Exception as err:
            print(f"保存历史记录时发生错误：{type(err).__name__}:{err}")

    def add(self, details: dict):
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

    def print_history(self):
        for index, item in enumerate(self.total_downloads):
            print(f"{index + 1}. <{item.get('jm_id')}> - {item.get('title')}")
            print(f"  作者：{item.get('author')}")
            print(f"  下载时间：{item.get('download_time')}")

    def get_latest(self):
        return self.total_downloads[-1] if self.total_downloads else None

    def get_recent(self, limit=10):
        return self.total_downloads[-limit:] if limit > 0 else self.total_downloads

    def clear_all(self):
        self.total_downloads = []
        self.save_all()


_history: DownloadHistory | None = None


def get_history() -> DownloadHistory:
    global _history
    if _history is None:
        _history = DownloadHistory()
    return _history


history = get_history()
