import os,time,sys

#测试模块下载功能用
#os.system("pip uninstall -y -q jmcomic")
#os.system("pip uninstall -y -q pyyaml")

menuText = \
"""\n\n-------------菜单-------------
1.菜单：显示此菜单页面
2.下载：下载JMcomic漫画
3.设置：设置文件路径等
4.关于：显示关于页面
5.检测：检测非内置模块是否导入
6.退出：退出程序
**输入数字以使用相关功能
------------------------------\n\n"""
jmLink = "https://github.com/hect0x7/JMComic-Crawler-Python"#JMcomic
yamlLink = "https://github.com/yaml/pyyaml"#pyYAML


def checkModule (moduleName,moduleLink,packName=None):
    packName = packName or moduleName
    try:
        module = __import__(packName)  
        print (f" {moduleName} 模块导入成功！") 
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
        except ModuleNotFoundError:#动态导入失败
            print (f"模块已安装但动态导入失败，请重启脚本或手动安装 {moduleName} 模块\n"+\
                   f"模块项目地址：{moduleLink}")
            sys.exit (0)
        else:#导入成功
            print (f" {moduleName} 模块导入成功！")
            return module
    

print (f"\n\n欢迎使用 JMcomic Downloader\n")
jm = checkModule ("jmcomic",jmLink)
yaml = checkModule ("pyYAML",yamlLink,"yaml")
print (f"{menuText}")


while True:
    command = input("\n请输入数字代号：")

    if command == "1":
        print (menuText)

    elif command == "2":
        jmID = input ("请输入禁漫车：")#todo-添加批量下载 空格分割jm号
        print ("\n下载即将开始...")
        try:
            jm.download_album (jmID)
        except:
            print ("\n**请求的本子不存在或请求时发生错误！")
        print ("\n下载结束！\n")
    
    elif command == "3":
        print("开发中...")

    elif command == "4":
        print("开发中...")

    elif command == "5":
        checkModule ("jmcomic",jmLink,)
        checkModule ("pyYAML",yamlLink,"yaml")

    elif command == "6":
        print("程序即将退出.")
        time.sleep (0.2)
        sys.exit(1)
    
    else:
        print (f"{menuText}\n指令不存在，请输入数字代号以使用相关功能！")
    


        