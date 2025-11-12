# pyright: ignore[reportPrivateImportUsage]

import traceback
import time
import sys
import re 

from libs import jmcomic as jm
from libs import yaml
from libs import InquirerPy
from libs.text import text



success_initialize = False
is_show_download_log = True


def initialize () -> bool:
    """检测配置文件；ver 为版本标识，exe(无需导入)/py"""
    try:
        print ("\n\n欢迎使用 JMcomic Downloader\n")
        is_initialized = True
    except Exception as err:
        print(f"初始化发生异常：{type(err).__name__}:{err}")
        is_initialized = False
    return is_initialized


def jmcomic_download() -> None:
    global 
    jm_ids = InquirerPy.inquirer.text(  # type: ignore
        message="请输入要下载的JMcomic车号（多个车号用空格分隔）：",
    ).execute()
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print ("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return
    jm_ids = jm_ids.strip().split ()
    is_permit = InquirerPy.inquirer.confirm(message=f"即将开始下载{jm_ids}，是否确认？",default=True).execute()  # type: ignore
    if not is_show_download_log:
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

def get_command(option) -> str:
    command = "1"
    if option == "menu":
        command = InquirerPy.inquirer.select(  # type: ignore
            message="\n请选择操作：",
            choices=[
                "1. 详细菜单","2. 下载漫画","3. 设置选项",
                "4. 关于项目","5. 退出程序"
            ],
        ).execute()
    elif option == "settings":
        command = InquirerPy.inquirer.select(  # type: ignore
            message="请选择设置项：",
            choices=[
                "1. 关闭下载日志输出",
            ],
        ).execute()
    return command[0]


def execute_command(command: str) -> None:
    if command == "1":
        print (text.menu)
    elif command == "2":
        jmcomic_download ()
    elif command == "3":
        command = get_command("settings")
        if command == "1":
            jm.disable_jm_log ()
            is_show_download_log = False
            print ("已关闭下载日志输出，若要开启，请重启程序")
        else:
            print (f"指令不存在，输入“1”以查看菜单")
    elif command == "4":
        print (text.about)
    elif command == "5":
        print ("程序即将退出")
        time.sleep (0.2)
        sys.exit (0)
    elif command == "0721":
        raise RuntimeError ("这是一个测试异常！")
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