import os
import sys
import simpsave as ss


default_cfgs = {"config_exsist":True,
                "show_download_log":True,
                "current_style_name":"默认风格",}


def get_config_path() -> str:
    """获取配置文件路径"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的可执行文件，配置文件放在可执行文件同目录
        base_dir = os.path.dirname(sys.executable)
    else:
        # 如果是源码运行，配置文件放在源码目录
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    config_path = os.path.join(base_dir, "config.yml")
    return config_path


class Configs:
    def __init__(self):
        self.config_file = get_config_path()
        try:
            ss.has("config_exsist", file=self.config_file)
        except FileNotFoundError:
            print(f"配置文件不存在，正在创建默认配置文件... ({self.config_file})")
            self.reset_cfg()
        except Exception as err:
            print(f"读取配置文件时发生未知异常：{type(err).__name__}:{err}")
        try:
            print(f"正在读取配置文件... ({self.config_file})")
            self.SHOW_JM_LOG = ss.read("show_download_log", file=self.config_file)
            self.CURRENT_STYLE_NAME = ss.read("current_style_name", file=self.config_file)
        except Exception as err:
            print(f"读取配置项时发生错误：{type(err).__name__}:{err}\n将使用默认配置，本次运行修改的设置可能不生效！")
            self.reset_cfg()

    def reset_cfg (self):
        """重置配置文件，全部变为默认项"""
        try:
            ss.delete(file = self.config_file) # 删除原有配置文件，write时会自动创建配置文件
            for key, val in default_cfgs.items():
                ss.write (key, val, file = self.config_file)
            self.SHOW_JM_LOG = default_cfgs["show_download_log"]
            self.CURRENT_STYLE_NAME = default_cfgs["current_style_name"]
        except Exception as err:
            print(f"初始化配置文件时发生错误：{type(err).__name__}:{err}")

    def edit (self, key: str, val):
        """编辑配置文件,并修改变量"""
        ss.write (key, val, file = self.config_file)
        return val
    
    def save_all(self):
        """将当前实例的配置写回配置文件"""
        try:
            self.edit("show_download_log", self.SHOW_JM_LOG)
            self.edit("current_style_name", self.CURRENT_STYLE_NAME)
        except Exception as err:
            print(f"保存配置时发生错误：{type(err).__name__}:{err}")


cfgs = Configs()