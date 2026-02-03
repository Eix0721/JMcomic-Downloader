import simpsave as ss



default_cfgs = {"config_exsist":True,
                "show_download_log":True,
                "current_style_name":"默认风格"}


class Configs:
    def __init__(self):
        try:
            ss.has("config_exsist", file="config.yml")
        except FileNotFoundError:
            print("配置文件不存在，正在创建默认配置文件...")
            Configs.reset_cfg(self)
        except Exception as err:
            print(f"读取配置文件时发生未知异常：{type(err).__name__}:{err}")
        try:
            self.SHOW_JM_LOG = ss.read("show_download_log", file="config.yml")
            self.CURRENT_STYLE_NAME = ss.read("current_style_name", file="config.yml")
        except Exception as err:
            print(f"读取配置项时发生错误：{type(err).__name__}:{err}\n将使用默认配置，本次运行修改的设置可能不生效！")
            Configs.reset_cfg(self)

    def reset_cfg (self):
        """重置配置文件，全部变为默认项"""
        try:
            ss.delete(file = "config.yml") # 删除原有配置文件，write时会自动创建配置文件
            for key, val in default_cfgs.items():
                ss.write (key, val, file = "config.yml")
            Configs.save_all(self)
        except Exception as err:
            print(f"初始化配置文件时发生错误：{type(err).__name__}:{err}")

    def edit (self, key: str, val):
        """编辑配置文件,并修改变量"""
        ss.write (key, val, file = "config.yml")
        return val
    
    def save_all(self):
        """将当前实例的配置写回配置文件"""
        try:
            Configs.edit(self, "show_download_log", self.SHOW_JM_LOG)
            Configs.edit(self, "current_style_name", self.CURRENT_STYLE_NAME)
        except Exception as err:
            print(f"保存配置时发生错误：{type(err).__name__}:{err}")

    
cfgs = Configs()