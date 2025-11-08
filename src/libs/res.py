import time
import sys
import os
import re

from typing import Optional
from types import ModuleType
from . import jmcomic as jm
from . import yaml
from .text import text


success_initialize = False


def check_module(module_name: str, 
                 module_link: str, 
                 pack_name: Optional[str]=None) -> ModuleType:
    """动态导入模块，若未安装则通过pip安装后再导入；
    module_name为模块名（下载使用），module_link为模块项目地址，
    pack_name为包名（导入用，与模块名不同才传入该参数）"""
    
    pack_name = pack_name or module_name

    try:
        module_import = __import__ (pack_name)
        print (f" {module_name} 模块导入成功！")
        return module_import
    
    except ModuleNotFoundError:
        command = input (f"\n未检测到 {module_name} 模块，将通过pip进行安装（Y/n）：")
        if command in ["","y","Y"]:  # 换行/y/Y同意安装
            print ("即将开始安装......")
            time.sleep (0.5)
            success_download = os.system (f"\"{sys.executable}\" -m pip install -q {module_name}")
        else:  # 不同意安装
            print (f"请安装 {module_name} 模块后使用\n"
                   f"模块项目地址：{module_link}")
            input("回车以退出程序...")
            sys.exit(0)

        if success_download != 0:  # pip安装失败
            print (f"模块安装失败，请手动安装 {module_name} 模块！\n"
                   f"模块项目地址：{module_link}")
            input("回车以退出程序...")
            sys.exit(0)
        # 安装成功，尝试再次导入
        try:
            module_import = __import__ (pack_name)
            print (f" {module_name} 模块导入成功！")
            return module_import
        except ModuleNotFoundError:  # 再次动态导入失败
            print(f"模块已安装但动态导入失败，请重启程序或手动安装 {module_name} 模块\n"
                  f"模块项目地址：{module_link}")
            input("回车以退出程序...")
            sys.exit(0)


def initialize () -> bool:
    """动态导入模块，检测配置文件；ver 为版本标识，exe(无需导入)/py"""
    # global jm
    # global yaml
    try:
        print ("\n\n欢迎使用 JMcomic Downloader\n")
        # if ver == "py":
            # jm = check_module("jmcomic", link.jm)
            # yaml = check_module("pyYAML", link.yaml, "yaml")
        # if os.path.exists("JMoption.yaml"):
        #     with open("JMopt.yaml", "r+", encoding="utf-8") as opt:
        #         opt = yaml.safe_load(opt)
        # else:
        #     print("配置文件不存在，已在当前目录创建 JMoption.yaml 文件")
        is_initialized = True
    except Exception as err:
        print(f"初始化发生异常：{type(err).__name__}:{err}")
        is_initialized = False
    return is_initialized


def jmcomic_download() -> None:
    jm_ids = input ("请输入禁漫车：")
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print ("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return
    jm_ids = jm_ids.strip().split ()
    print (f"开始下载：{jm_ids}")
    start_time = time.time()
    try:
        jm.download_album(jm_ids)
    except Exception as err:
        print ("\n**本子不存在或请求时发生错误:"
            f"{type(err).__name__}:{err}\n")
    else:
        end_time = time.time()
        print (f"\n下载成功！\n用时:{end_time - start_time:.3f}秒\n")


def execute_command(command: str) -> None:
    if command == "1":
        print (text.menu)
    elif command == "2":
        jmcomic_download ()
    elif command == "3":
        command = input (f"\n{text.settings}\n\n请输入数字代号:")
        if command == "1":
            jm.disable_jm_log ()
            print ("已关闭下载日志输出，若要开启，请重启程序")
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
