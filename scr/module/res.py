import time
import sys
import os

from typing import Optional
from types import ModuleType

from . import jmcomic as jm
from . import yaml


success_initialize = False

class link:
    jm = "https://github.com/hect0x7/JMComic-Crawler-Python"  # JMcomic
    yaml = "https://github.com/yaml/pyyaml"  # pyYAML
    pj = "https://github.com/Eix0721/JMcomic-Downloader"
class text:
    menu = f"""
    \n\n{"-" * 18}菜单{"-" * 18}
    1.菜单：显示此菜单页面
    2.下载：下载JMcomic漫画
        ╰以空格分割多个禁漫车以批量下载
    3.设置：设置文件路径等（开发中）
    4.关于：显示关于页面
    5.退出：退出程序
    **输入数字以使用相关功能\n{"-" * 40}\n
    """

    settings = f"""
    \n\n{"-" * 18}设置{"-" * 18}
    1.日志：关闭下载日志输出
    **输入数字以使用相关功能\n{"-" * 40}\n
    """

    about = f"""
\n\n感谢您使用JMcomic Downloader！本项目由Eix0721开发
仓库地址：{link.pj}

本项目使用了以下第三方库：
**JMComic Crawler Python
描述：提供漫画下载的核心功能
地址：{link.jm}
**pyYAML
描述：未来将用于配置文件支持
地址：{link.yaml}

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
JMcomic 也是一款十分优秀的漫画软件，关爱禁漫娘，请不要一次性下载过多本子!
"""


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
    jm_ids = input ("请输入禁漫车：").strip().split()
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


if __name__ == "__main__":
    input ("本模块不可单独运行，请运行主程序文件！回车以退出...")
