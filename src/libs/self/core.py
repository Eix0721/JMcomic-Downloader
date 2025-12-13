import re
import sys
import time
import traceback
import jmcomic as jm


from libs.self import ui
from libs.self.text import Text


success_initialize = False
show_download_log = True



class get_command:
    def menu(self):
        command = ui.select_choice (message="\n请选择操作：",
                                    choices=["详细菜单","下载漫画","设置选项",
                                            "切换主题","关于项目","退出程序"])
        return command
    def settings (self):
        command = ui.select_choice (message="请选择设置项：",
                                    choices=[f"{'开启' if not show_download_log else '关闭'}下载日志输出","设置选项","退出设置"])
        return command


def initialize () ->bool:
    try:
        print ("\n\n欢迎使用 JMcomic Downloader\n")
        jmcli = jm.JmModuleConfig.option_class().default().build_jm_client() # 初始化 jmcomic 客户端
        is_initialized = True
    except Exception as err:
        print(f"初始化发生异常：{type(err).__name__}:{err}")
        is_initialized = False
    return is_initialized


def jmcomic_download() ->None:
    global show_download_log,global_style
    jm_ids = ui.input_text("请输入要下载的 JMcomic 车号（多个车号用空格分隔）：")
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print ("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return
    jm_ids = jm_ids.strip().split ()
    is_permit = ui.confirm_yes_no(f"即将下载：{jm_ids}，是否继续？")
    if not show_download_log:
        print ("下载任务已开始，请耐心等待...")
    if is_permit:
        start_time = time.time()
        try:
            jm.download_album(jm_ids)
        except Exception as err:
            print ("\n**本子不存在或请求时发生错误:"
                  f"{type(err).__name__}:{err}\n")
        else:
            print (f"\n下载完成！\n用时:{time.time() - start_time:.3f}秒\n")  
    else:
        print ("已取消下载任务。")
    

def setting ():
    global show_download_log
    while True:
        command = get_command().settings()
        
        if command == f"{'开启' if not show_download_log else '关闭'}下载日志输出":
            if show_download_log:
                jm.disable_jm_log ()
                show_download_log = False
            else:
                jm.JmModuleConfig.FLAG_ENABLE_JM_LOG = True
                show_download_log = True
            print (f"已{'开启' if show_download_log else '关闭'}下载日志输出。\n")
        elif command == "设置选项":
            print (f"{Text.settings}\n")
        elif command == "退出设置":
            break
        else:
            print (f"指令 \"{command}\" 不存在或不可用。")


def execute_command(command: str) ->None:
    if command == "详细菜单":
        print (Text.menu)
    elif command == "下载漫画":
        jmcomic_download ()
    elif command == "设置选项":
        setting()
    elif command == "切换主题":
        ui.set_style()
    elif command == "关于项目":
        print (Text.about)
    elif command == "退出程序":
        print ("程序即将退出")
        time.sleep (0.5)
        sys.exit (0)
    else:
        print (f"指令\"{command}\"不存在或不可用。")


def main():
    if not initialize():
        input("回车以退出程序...")
        return  
    print (Text.menu)
    while True:
        try:
            execute_command (get_command().menu())
        except Exception as err:
            print (f"\n程序发生异常：{type(err).__name__}:{err}\n")
            input("回车以查看详细报错...")
            traceback.print_exc()