# 标准库
import datetime
from os import write
from typing import List
# 第三方库
import simpsave as ss

from libs.self import ui


default_history = {
    "history_exist": True,
    "total_downloads": [],   # 总下载次数--格式{"jm_id": int, "title": str, "time": str}
}


class DownloadHistory:
    def __init__(self):
        try: # 检查历史记录文件是否存在
            ss.has("history_exist", file="history.yml")
        except FileNotFoundError:
            print("历史记录文件不存在，正在创建默认历史记录文件...")
            DownloadHistory.reset_history(self)
        except Exception as err:
            print(f"读取历史记录文件时发生未知异常：{type(err).__name__}:{err}")
        
        try: # 读取历史记录项
            print("正在读取历史记录文件...")
            self.TOTAL_DOWNLOADS: List[dict] = ss.read("total_downloads", file="history.yml")
        except FileNotFoundError:
            print("历史记录文件不存在，正在创建默认历史记录文件...")
            DownloadHistory.reset_history(self)
        except Exception as err:
            print(f"读取历史记录项时发生错误：{type(err).__name__}:{err}")
            if ui.confirm("您可以将问题反馈给开发者并备份history.yml\n也可以重置历史记录文件（不推荐），是否重置？"):
                DownloadHistory.reset_history(self)
            else:
                input ("请反馈并手动备份history.yml！按回车键退出程序...")
                exit(1)

    def reset_history(self):
        """重置历史记录文件，全部变为默认项"""
        try:
            ss.delete(file="history.yml")  # 删除原有历史记录文件，write时会自动创建文件
            self.TOTAL_DOWNLOADS = DownloadHistory.edit(self, "total_downloads", [])
        except Exception as err:
            print(f"初始化历史记录文件时发生错误：{type(err).__name__}:{err}")

    def edit(self, key: str, val):
        """编辑历史记录文件,并修改变量"""
        ss.write(key, val, file="history.yml")
        return val
    
    def save_all(self):
        """将当前实例的历史记录写回文件"""
        try:
            DownloadHistory.edit(self, "total_downloads", self.TOTAL_DOWNLOADS)
        except Exception as err:
            print(f"保存历史记录时发生错误：{type(err).__name__}:{err}")

    def add (self,details: dict):
        """添加下载记录，并返回最新记录"""
        self.TOTAL_DOWNLOADS.append({
            "jm_id": details.get("id"),
            "title": details.get("title"),
            "author":details.get("author"),
            "download_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })
        DownloadHistory.save_all(self)
        return self.TOTAL_DOWNLOADS[-1]
    
    def print_history (self):
        for index, item in enumerate(self.TOTAL_DOWNLOADS):
            print (f"{index + 1}. <{item.get('jm_id')}> - {item.get('title')}\n作者：{item.get('author')}\n下载时间：{item.get('download_time')}")


    def get_latest (self):
        """获取最新的下载记录"""
        return self.TOTAL_DOWNLOADS[-1] if self.TOTAL_DOWNLOADS else None
    
    def get_TOTAL_DOWNLOADS(self, limit=10):
        """获取最近的下载记录"""
        return self.TOTAL_DOWNLOADS[-limit:] if limit > 0 else self.TOTAL_DOWNLOADS

    def clear_TOTAL_DOWNLOADS(self):
        """清空最近下载记录"""
        self.TOTAL_DOWNLOADS = []
        DownloadHistory.save_all(self)

    def clear_all(self):
        """清空所有历史记录"""
        self.TOTAL_DOWNLOADS = []
        DownloadHistory.save_all(self)


# 创建全局历史记录实例
history = DownloadHistory()
