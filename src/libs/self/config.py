import simpsave as ss

default_cfg = {"config_exsist":True,
                "show_download_log":True,
               "current_style_name":"默认风格"}

def init_cfg ():
    """初始化配置文件"""
    try:
        ss.delete(file = "config.yml")
        for key, val in default_cfg.items():
            ss.write (key, val, file = "config.yml")
    except Exception as err:
        print(f"初始化配置文件时发生错误：{type(err).__name__}:{err}")

def edit (key: str, val):
    """编辑配置文件,并修改变量"""
    ss.write (key, val, file = "config.yml")
    return val

try:
    ss.has ("config_exsist", file = "config.yml")
except FileNotFoundError:
    print("配置文件不存在，正在创建默认配置文件...")
    init_cfg()
else:
    SHOW_JM_LOG = ss.read("show_download_log", file = "config.yml")
    CURRENT_STYLE_NAME = ss.read("current_style_name", file = "config.yml") 