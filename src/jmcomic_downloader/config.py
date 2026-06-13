import os
import sys

import simpsave as ss


def _get_config_path() -> str:
    """获取配置文件路径"""
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "config.yml")


class Configs:
    def __init__(self):
        self.config_file = _get_config_path()
        self.show_jm_log = True
        self.current_style_name = "默认风格"

    def load(self):
        try:
            ss.has("config_exsist", file=self.config_file)
        except FileNotFoundError:
            print(f"配置文件不存在，正在创建默认配置文件... ({self.config_file})")
            self.reset()
            return
        except Exception as err:
            print(f"读取配置文件时发生未知异常：{type(err).__name__}:{err}")

        try:
            print(f"正在读取配置文件... ({self.config_file})")
            self.show_jm_log = ss.read("show_download_log", file=self.config_file)
            self.current_style_name = ss.read("current_style_name", file=self.config_file)
        except Exception as err:
            print(f"读取配置项时发生错误：{type(err).__name__}:{err}")
            print("将使用默认配置，本次运行修改的设置可能不生效！")
            self.reset()

    def reset(self):
        try:
            ss.delete(file=self.config_file)
            for key, val in self._defaults().items():
                ss.write(key, val, file=self.config_file)
            self.show_jm_log = True
            self.current_style_name = "默认风格"
        except Exception as err:
            print(f"初始化配置文件时发生错误：{type(err).__name__}:{err}")

    def edit(self, key: str, val):
        ss.write(key, val, file=self.config_file)
        return val

    def save_all(self):
        try:
            self.edit("show_download_log", self.show_jm_log)
            self.edit("current_style_name", self.current_style_name)
        except Exception as err:
            print(f"保存配置时发生错误：{type(err).__name__}:{err}")

    @staticmethod
    def _defaults():
        return {
            "config_exsist": True,
            "show_download_log": True,
            "current_style_name": "默认风格",
        }


_cfgs: Configs | None = None


def get_config() -> Configs:
    global _cfgs
    if _cfgs is None:
        _cfgs = Configs()
    return _cfgs


cfgs = get_config()
