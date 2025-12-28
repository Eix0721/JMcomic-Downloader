#标准库
from calendar import c
from email import message
import re                           
import sys
import time
import traceback
#第三方库
import jmcomic as jm         
#本地库       
import libs.self.config as config   
from libs.self import ui
from libs.self import text
from libs.self.config import show_download_log


def create_jmcli() -> jm.JmcomicClient: # 初始化并构建 JMcomic 客户端
    return jm.JmModuleConfig.option_class().default().build_jm_client() 

def show_status(arg: bool) -> str: # True -> '开启'
    return "开启" if arg else "关闭" 

def jmcomic_download() -> None:
    """
    包含：输入校验、用户确认、执行下载、异常处理
    """
    global show_download_log 
    jm_ids = ui.input_text("请输入要下载的 JMcomic 车号（多个车号用空格分隔）：")
    # 正则校验，仅允许数字和空格
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return
    # 去头尾空格，并分割为list
    jm_ids = jm_ids.strip().split()
    is_permit = ui.confirm (f"即将下载：{jm_ids}，是否继续？")
    
    if is_permit:
        # 未开启详细日志，提示等待
        if not show_download_log:
            print("下载任务已开始，请耐心等待...")

        start_time = time.time()
        try:
            jm.download_album(jm_ids)
        except Exception as err:
            print("\n**本子不存在或请求时发生错误:")
            print(f"{type(err).__name__}:{err}\n")
        else:
            print(f"\n下载结束！\n用时:{time.time() - start_time:.3f}秒\n")  
    else:
        print("已取消下载任务。")


def setting() -> None:
    global show_download_log
    command = f"{show_status(show_download_log)}下载日志输出" # 默认选项
    while True:
        command = ui.select (message="请选择设置项：",
                            choices=text.SETTING_SECTIONS,
                            default= command)
        if command == f"{show_status(show_download_log)}下载日志输出":
            if show_download_log:
                jm.disable_jm_log()
                show_download_log = False
            else:
                # 如果当前是关闭，则开启
                jm.JmModuleConfig.FLAG_ENABLE_JM_LOG = True
                show_download_log = True
            text.SETTING_SECTIONS[text.SETTING_SECTIONS.index(
                                f"{show_status(not show_download_log)}下载日志输出")] = command
            print(f"已{show_status(show_download_log)}下载日志输出。\n")   
        elif command == "设置选项":
            print(f"{text.TEXT['settings']}\n")
        elif command == "退出设置":
            break
        else:
            print(f"指令 \"{command}\" 不存在或不可用。")

def execute_command(command: str) -> None:
    if command == "详细菜单":
        print(text.TEXT["menu"])
    elif command == "下载漫画":
        jmcomic_download()
    elif command == "设置选项":
        setting()
    elif command == "切换主题":
        ui.set_style() 
    elif command == "关于项目":
        print(text.TEXT["about"])
    elif command == "退出程序":
        print("程序即将退出")
        time.sleep(0.5)
        sys.exit(0)
    else:
        print(f"指令\"{command}\"不存在或不可用。")

def main():
    try:
        user_choice = "详细菜单" # 初始化预留位
    except Exception as err:
        print(f"初始化发生异常：{type(err).__name__}:{err}")
        traceback.print_exc()
        return
    print(f"欢迎使用 JMcomic Downloader！\n{text.TEXT['menu']}")
    while True:
        try:
            # 获取用户选择并执行
            user_choice = ui.select (message= "请选择操作：",
                                     choices= text.MENU_SECTIONS,
                                     default= user_choice)
            execute_command(user_choice)
        except Exception as err:
            print(f"\n程序发生异常：{type(err).__name__}:{err}\n")
            input("回车以查看详细报错...")
            traceback.print_exc()