"""
jmcomic模块使用文档：https://jmcomic.readthedocs.io/zh-cn/latest/tutorial/0_common_usage/
To-Do：添加下载前显示本子标题；YAML文件配置；Github README页面
"""

import os,time,sys
#仅开发时使用↓
#import jmcomic as jm
#测试模块下载功能用↓
#os.system("pip uninstall -y -q jmcomic")
#os.system("pip uninstall -y -q pyyaml")

def checkModule (moduleName,moduleLink,packName=None):
    packName = packName or moduleName
    try:
        module = __import__(packName)  
        print (f" {moduleName} 模块导入成功！")
        return module 
    except ModuleNotFoundError:
        command = input (f"\n未检测到 {moduleName} 模块，将通过pip进行安装（Y/n）：")
        if command.lower() == "y":#pip安装
            print ("即将开始安装......")
            time.sleep (0.5)
            successDnld = os.system (f"\"{sys.executable}\" -m pip install -q {moduleName}")
        else:#不同意安装
            print (f"请安装 {moduleName} 模块后使用\n"+\
                   f"模块项目地址：{moduleLink}")
            sys.exit (0)
        if successDnld != 0:#pip安装失败
            print (f"模块安装失败，请手动安装 {moduleName} 模块！\n"+\
                   f"模块项目地址：{moduleLink}")
            sys.exit (0)
        try:
            module =  __import__ (packName)
            print (f" {moduleName} 模块导入成功！")
            return module
        except ModuleNotFoundError:#动态导入失败
            print (f"模块已安装但动态导入失败，请重启脚本或手动安装 {moduleName} 模块\n"+\
                   f"模块项目地址：{moduleLink}")
            sys.exit (0)

def printWd (text,speed=None):
    speed = speed or 0.002#默认0.002s
    for wd in text:
        print (wd,end="")
        time.sleep(speed)
    print()

jmLink = "https://github.com/hect0x7/JMComic-Crawler-Python"#JMcomic
yamlLink = "https://github.com/yaml/pyyaml"#pyYAML
pjLink = "https://github.com/Eix0721/JMcomic-Downloader"
menuText = \
f"""\n\n{"-"*18}菜单{"-"*18}
1.菜单：显示此菜单页面
2.下载：下载JMcomic漫画
        ╰批量下载以空格分割多个禁漫车
3.设置：设置文件路径等
4.关于：显示关于页面
5.检测：检测非内置模块是否导入
        ╰目前检测jmcomic,pyYAML模块
6.退出：退出程序
**输入数字以使用相关功能\n{"-"*40}\n\n"""
aboutText = \
f"""\n\n感谢您使用JMcomic Downloader！
本项目由Eix_开发
仓库地址：{pjLink}

本项目使用了以下第三方库：
**JMComic Crawler Python
描述：是本项目的灵感来源及下载功能的基石！
地址：{jmLink}
**pyYAML
描述：用于下载的各项配置功能。
地址：{yamlLink}

诚挚感谢以上项目的开发者与贡献者为开源社区作出的奉献！
"""

try:
    printWd (f"\n\n欢迎使用 JMcomic Downloader\n",0.02)
    jm = checkModule ("jmcomic",jmLink)
    yaml = checkModule ("pyYAML",yamlLink,"yaml")
    printWd (f"{menuText}")
except:
    print ("程序初始化失败！")
    sys.exit (0)


while True:
    command = input("\n请输入数字代号：")

    if command == "1":
        printWd (menuText)

    elif command == "2":
        jmIDs = input ("请输入禁漫车：")
        if " " in jmIDs:#分割多个禁漫车
            jmIDs = jmIDs.split()
            print (f"检测到多个禁漫车，即将下载\n{jmIDs}")
        printWd ("\n下载即将开始...",0.008)
        try:
            jm.download_album (jmIDs)
        except:
            print ("\n**请求的本子不存在或请求时发生错误！")
        print ("\n下载结束！\n")
    
    elif command == "3":
        print("开发中...")

    elif command == "4":
        printWd (aboutText)

    elif command == "5":
        checkModule ("jmcomic",jmLink,)
        checkModule ("pyYAML",yamlLink,"yaml")

    elif command == "6":
        print("程序即将退出.")
        time.sleep (0.2)
        sys.exit(0)
    
    else:
        printWd (f"{menuText}\n指令不存在，请输入数字代号以使用相关功能！")
    


        