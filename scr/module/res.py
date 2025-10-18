import time,sys,os
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
successInitialize = False
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
f"""\n\n感谢您使用JMcomic Downloader！本项目由Eix0721开发
仓库地址：{pjLink}

本项目使用了以下第三方库：
**JMComic Crawler Python
描述：提供漫画下载的核心功能
地址：{jmLink}
**pyYAML
描述：未来将用于配置文件支持
地址：{yamlLink}

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
JMcomic 也是一款十分优秀的漫画软件，关爱禁漫娘，请不要一次性下载过多本子!
"""
