import traceback
import time
import sys
import re 
import os

from libs import jmcomic as jm
from libs import yaml
from libs import InquirerPy
from libs.InquirerPy import inquirer,utils
from libs.text import text, infurce_style



success_initialize = False
is_show_download_log = True
global_style = InquirerPy.get_style (infurce_style.all_styles["默认风格"],style_override=True)



def initialize () ->bool:
    try:
        print ("\n\n欢迎使用 JMcomic Downloader\n")
        is_initialized = True
    except Exception as err:
        print(f"初始化发生异常：{type(err).__name__}:{err}")
        is_initialized = False
    return is_initialized


def jmcomic_download() ->None:
    global is_show_download_log,global_style
    jm_ids = InquirerPy.inquirer.text(  # type: ignore
        message="请输入要下载的JMcomic车号（多个车号用空格分隔）：",
        style = global_style,
        pointer = ">"
    ).execute()
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print ("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return
    jm_ids = jm_ids.strip().split ()
    is_permit = InquirerPy.inquirer.confirm(message=f"即将开始下载{jm_ids}，是否确认？",# type: ignore
                                            default=True,style = global_style,pointer = ">").execute()  
    if not is_show_download_log:
        print ("已关闭下载日志输出，若要开启，请重启程序")
        print ("下载任务已开始，请耐心等待...")

    if is_permit:
        start_time = time.time()
        try:
            jm.download_album(jm_ids)
        except Exception as err:
            print ("\n**本子不存在或请求时发生错误:"
                f"{type(err).__name__}:{err}\n")
        else:
            end_time = time.time()
            print (f"\n下载成功！\n用时:{end_time - start_time:.3f}秒\n")
    else:
        print ("已取消下载任务。")

def set_style() ->None:
    global global_style
    is_keep_going = True
    style_choice = "默认风格"
    while is_keep_going:
        try:
            style_choices = list(infurce_style.all_styles.keys()) + ["取消"]
            style_choice = InquirerPy.inquirer.select(  # type: ignore
                message = "请选择界面风格：",
                choices = style_choices,
                default = style_choice,
                style = global_style,
                pointer = ">"
            ).execute()
            if style_choice == "取消":
                is_keep_going = False
                return
            style_args = infurce_style.all_styles[style_choice]
            global_style = InquirerPy.get_style (style_args,style_override=True)
        except Exception as err:
            print(f"切换样式时发生错误：{type(err).__name__}:{err}")
            break


def get_command(option) ->str:
    global global_style
    command = ""
    if option == "menu":
        command = InquirerPy.inquirer.select(   # type: ignore
            message="\n请选择操作：",
            choices=[
                "详细菜单","下载漫画","设置选项",
                "切换主题","关于项目","退出程序"
            ],
            style = global_style,
            pointer = ">"
        ).execute()
    elif option == "settings":
        command = InquirerPy.inquirer.select(  # type: ignore
            message="请选择设置项：",
            choices=[
                "关闭下载日志输出","退出设置"
            ],
            style = global_style,
            pointer = ">"
        ).execute()
    return command


def execute_command(command: str) ->None:
    global is_show_download_log,global_style
    if command == "详细菜单":
        print (text.menu)
    elif command == "下载漫画":
        jmcomic_download ()
    elif command == "设置选项":
        is_in_settings = True
        while is_in_settings:
            command = get_command("settings")
            if command == "关闭下载日志输出":
                jm.disable_jm_log ()
                is_show_download_log = False
                print ("已关闭下载日志输出，若要开启，请重启程序")
            if command == "退出设置":
                is_in_settings = False
            else:
                print (f"指令不存在，输入“1”以查看菜单")
    elif command == "切换主题":
        set_style()
    elif command == "关于项目":
        print (text.about)
    elif command == "退出程序":
        print ("程序即将退出")
        time.sleep (0.2)
        sys.exit (0)
    else:
        print (f"指令不存在，输入“1”以查看菜单")


def main():
    if not initialize():
        input("回车以退出程序...")
        return  
    print (text.menu)
    while True:
        try:
            command = get_command("menu")
            execute_command (command)
        except Exception as err:
            print (f"\n程序发生异常：{type(err).__name__}:{err}\n")
            command = input("回车以查看详细报错...")
            traceback.print_exc()