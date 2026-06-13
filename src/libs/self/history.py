import datetime

import simpsave as ss

from libs.self import ui


default_history = {
    "history_exist": True,
    "total_downloads": [],   # 总下载次数--格式{"jm_id": int, "title": str, "time": str}
}


class DownloadHistory:
    def __init__(self):
        try:
            ss.has("history_exist", file="history.yml")
        except FileNotFoundError:
            print("历史记录文件不存在，正在创建默认历史记录文件...")
            self.reset_history()
        except Exception as err:
            print(f"读取历史记录文件时发生未知异常：{type(err).__name__}:{err}")

        try:
            print("正在读取历史记录文件...")
            self.TOTAL_DOWNLOADS: list[dict] = ss.read("total_downloads", file="history.yml")
        except FileNotFoundError:
            print("历史记录文件不存在，正在创建默认历史记录文件...")
            self.reset_history()
        except Exception as err:
            print(f"读取历史记录项时发生错误：{type(err).__name__}:{err}")
            if ui.confirm("您可以将问题反馈给开发者并备份history.yml\n也可以重置历史记录文件（不推荐），是否重置？"):
                self.reset_history()
            else:
                input("请反馈并手动备份history.yml！按回车键退出程序...")
                exit(1)

    def reset_history(self):
        try:
            ss.delete(file="history.yml")
            self.TOTAL_DOWNLOADS = self.edit("total_downloads", [])
        except Exception as err:
            print(f"初始化历史记录文件时发生错误：{type(err).__name__}:{err}")

    def edit(self, key: str, val):
        """编辑历史记录文件,并修改变量"""
        ss.write(key, val, file="history.yml")
        return val
    
    def save_all(self):
        try:
            self.edit("total_downloads", self.TOTAL_DOWNLOADS)
        except Exception as err:
            print(f"保存历史记录时发生错误：{type(err).__name__}:{err}")

    def add(self, details: dict):
        self.TOTAL_DOWNLOADS.append({
            "jm_id": details.get("id"),
            "title": details.get("title"),
            "author": details.get("author"),
            "download_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        self.save_all()
        return self.TOTAL_DOWNLOADS[-1]

    def print_history(self):
        for index, item in enumerate(self.TOTAL_DOWNLOADS):
            print(f"{index + 1}. <{item.get('jm_id')}> - {item.get('title')}\n作者：{item.get('author')}\n下载时间：{item.get('download_time')}")

    def get_latest(self):
        return self.TOTAL_DOWNLOADS[-1] if self.TOTAL_DOWNLOADS else None

    def get_recent(self, limit=10):
        return self.TOTAL_DOWNLOADS[-limit:] if limit > 0 else self.TOTAL_DOWNLOADS

    def clear_all(self):
        self.TOTAL_DOWNLOADS = []
        self.save_all()


# 创建全局历史记录实例
history = DownloadHistory()
