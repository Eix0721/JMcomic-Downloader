# Copyright (c) 2025 Eix0721
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import os,time,sys,yaml,jmcomic as jm
from module.res import *

#仅开发时使用↓
#import jmcomic as jm,yaml
#测试模块下载功能用↓
#os.system("pip uninstall -y -q jmcomic")
#os.system("pip uninstall -y -q pyyaml")


while __name__ == "__main__":
    try:#动态导入jmcomic,yaml，检测配置文件
        printWd (f"\n\n欢迎使用 JMcomic Downloader\n",0.02)
        #jm = checkModule ("jmcomic",jmLink)
        #yaml = checkModule ("pyYAML",yamlLink,"yaml")
        printWd (f"{menuText}")
    except Exception as err:
        print (f"初始化异常！错误信息：{type(err).__name__}:{err}")
        successInitialize = False
    else:
        successInitialize = True

    try:
        while successInitialize:
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
                print("程序即将退出")
                time.sleep (0.2)
                sys.exit(0)
            
            elif command == "0721":#触发报错
                1/0

            else:
                printWd (f"{menuText}\n指令不存在，请输入数字代号以使用相关功能！")
    except Exception as err:
        printWd ("\n程序发生异常！\n错误描述："+\
                f"{type(err).__name__}:{err}\n"+\
                f"这个蠢货又写bug了（）请在\n{pjLink}\n创建issue喵awa")
        input ("回车以继续...")