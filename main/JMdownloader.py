import os,time

menuText = \
    "\n\n----------菜单----------\n"+\
    "1.菜单：显示此菜单栏\n2.下载：下载JMcomic漫画\n"+\
    "3.设置：设置文件路径等\n4.关于：显示关于页面\n"+\
    "5.退出：退出程序\n"+\
    "**输入数字以使用相关功能\n------------------------\n\n"
moduleLink = "https://github.com/hect0x7/JMComic-Crawler-Python"

#检查模块是否存在
def checkModule (moduleName):
    try:
        module = __import__(moduleName)
        return module
    except ModuleNotFoundError:
        command = input ("未检测到\"JMcomic\"模块，将通过pip进行安装（y/n）：")
        if command == "y":
            print ("即将开始安装：")
            time.sleep (0.5)
            os.system ("{os.sys.executable} -m pip install jmcomic")
            print ("\n\n安装结束，如未生效，请手动安装\"jmcomic\"模块\n"+\
                f"（JMcomic模块项目地址：{moduleLink}\n{menuText}）")
        else:
            print ("请安装\"jmcomic\"模块后使用\n"+\
                   f"（JMcomic模块项目地址：{moduleLink}）")
            exit ()




print (f"\n\n欢迎使用 JMcomic Downloader\n{menuText}")
jm = checkModule ("jmcomic")

while True:
    command = input("请输入数字代号：")

    if command == "1":
        print (menuText)

    elif command == "2":
        jmID = input ("请输入禁漫车：")
        #含空格则分割至列表
        #if " " in jmID:
        print ("下载即将开始...")
        jm.download_album (jmID)
        print ("下载完成！\n")
    
    elif command == "3":
        print("开发中...")

    elif command == "4":
        print("开发中...")
    
    elif command == "5":
        print("程序即将退出.")
        time.sleep (1)
        exit()
    


        