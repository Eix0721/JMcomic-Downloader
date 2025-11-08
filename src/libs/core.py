from libs.res import initialize,execute_command,text
import traceback

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
            command = input("键入\"Y\"以查看详细报错：")
            if command.strip().upper() == "Y":
                traceback.print_exc()