# Copyright (c) 2025 Eix0721
# Licensed under the MIT License. See LICENSE file in the project root for full license information.


from module.res import initialize,execute_command,text

def main():
    if not initialize():
        input("回车以退出程序...")
        return
    print (text.menu)
    while True:
        try:
            command = input ("\n请输入数字代号：")
            execute_command (command)
        except Exception as err:
            print ("\n程序发生异常："
                  f"{type(err).__name__}:{err}\n")
            input ("回车以继续...")


if __name__ == "__main__":
    main()
