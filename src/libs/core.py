from email import message
import traceback
import time
import sys
import re 
import os
import libs.ui as ui

from libs import InquirerPy, jmcomic as jm
from libs import yaml
from libs.text import text, infurce_style



success_initialize = False
is_show_download_log = True



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
    jm_ids = ui.input_text("请输入要下载的 JMcomic 车号（多个车号用空格分隔）：")
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print ("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return
    jm_ids = jm_ids.strip().split ()
    is_permit = ui.confirm_yes_no(f"即将下载：{jm_ids}，是否继续？")
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


def get_command(option) ->str:
    global global_style
    command = ""
    if option == "menu":
        command = ui.select_choice (
            message="\n请选择操作：",
            choices=["详细菜单","下载漫画","设置选项",
                    "切换主题","关于项目","退出程序"])
    elif option == "settings":
        command = ui.select_choice (
                message="请选择设置项：",
                choices=["关闭下载日志输出","退出设置"])
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
        ui.set_style()
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