# 标准库
import re                           
import sys
import time
import traceback
# 第三方库
import jmcomic as jm         
# 本地库
import libs.self.ui as ui
from libs.self import text
from libs.self.config import cfgs
from libs.self.history import history
from libs.self.test_domain import test_all_domains


def create_jmcli() -> jm.JmcomicClient: # 初始化并构建 JMcomic 客户端
    return jm.JmModuleConfig.option_class().default().build_jm_client() 

def show_status(arg: bool) -> str: # True -> '开启'
    return "开启" if arg else "关闭" 

def excute_detail (arg) ->dict:
    return {"title": arg.name,
            "id":    arg.id,
            "author":arg.author,
            "tags":  arg.tags,
            "pages": arg.page_count,
            "chapters": len(arg)}

def jmcomic_download() -> None:
    """
    包含：输入校验、用户确认、执行下载、异常处理
    """
    global SHOW_JM_LOG 
    jm_ids = ui.input_text("请输入要下载的 JMcomic 车号（多个车号用空格分隔）：")
    # 正则校验，仅允许数字和空格
    if not re.fullmatch(r"(\d+\s*)+", jm_ids):
        print("输入的格式有误，请输入仅包含数字的车号，多个车号用空格分隔！")
        return

    if ui.confirm (f"即将下载：{jm_ids}，是否继续？"):
        # 未开启详细日志，提示等待
        if not cfgs.SHOW_JM_LOG:
            print("下载任务已开始，请耐心等待...")

        start_time = time.time()
        for jm_id in jm_ids.strip().split():
            try:
                album_detail = excute_detail(jm.download_album(jm_id)[0]) # type: ignore 
            except Exception as err:
                print("\n**本子不存在或请求时发生错误:")
                print(f"{type(err).__name__}:{err}\n")
            else:
                latest = history.add(album_detail)
                print(f"[{latest.get('download_time')}] <{latest.get('jm_id')}> {latest.get('title')} 下载完成！")  
        print (f"所有下载任务已完成，耗时 {time.time() - start_time:.2f} 秒。\n")
    else:
        print("已取消下载任务。")


def setting() -> None:
    command = f"{show_status(not cfgs.SHOW_JM_LOG)}下载日志输出" # 默认选项
    while True:
        command = ui.select (message="请选择设置项：",
                            choices=text.SETTING_SECTIONS,
                            default= command)
        if command == f"{show_status(not cfgs.SHOW_JM_LOG)}下载日志输出":
            # ONLY DEBUG ↓↓↓
            # print(f"TEXT:{text.SETTING_SECTIONS}\nFLAG:{jm.JmModuleConfig.FLAG_ENABLE_JM_LOG}\ncfgs:{cfgs.SHOW_JM_LOG}")
            jm.JmModuleConfig.FLAG_ENABLE_JM_LOG = not jm.JmModuleConfig.FLAG_ENABLE_JM_LOG
            cfgs.SHOW_JM_LOG = cfgs.edit("show_download_log",jm.JmModuleConfig.FLAG_ENABLE_JM_LOG)
            # 修改相关选项的状态
            text.SETTING_SECTIONS[text.SETTING_SECTIONS.index(command)] = f"{show_status(not cfgs.SHOW_JM_LOG)}下载日志输出"
            print(f"已{show_status(cfgs.SHOW_JM_LOG)}下载日志输出。\n")  
            # ONLY DEBUG ↓↓↓
            # print(f"TEXT:{text.SETTING_SECTIONS}\nFLAG:{jm.JmModuleConfig.FLAG_ENABLE_JM_LOG}\ncfgs:{cfgs.SHOW_JM_LOG}")
        elif command == "测试连接":
            print("正在测试当前IP可访问的Jmcomic域名，请稍候...")
            test_all_domains()
            print("测试完成。\n") 
        elif command == "恢复默认":
            if ui.confirm("此操作将重置所有设置且不可逆，确认恢复默认设置？"):
                cfgs.reset_cfg()
                print("已恢复默认设置，请重新启动程序以应用更改。\n")
            else:
                print("已取消操作。\n")
        elif command == "切换主题":
            ui.set_style() 
        elif command == "设置说明":
            print(f"{text.TEXT['settings']}\n")
        elif command == "退出设置":
            break
        else:
            print(f"指令 \"{command}\" 不存在或不可用。")

def execute_command(command: str) -> None:
    if command == "功能说明":
        print(text.TEXT["menu"])
    elif command == "下载漫画":
        jmcomic_download()
    elif command == "设置选项":
        setting()
    elif command == "历史记录":
        history.print_history()
    elif command == "关于项目":
        for ln in text.TEXT["about"].splitlines():
            print(ln, flush=True)
            time.sleep(0.03)
    elif command == "退出程序":
        print("程序即将退出")
        time.sleep(0.5)
        sys.exit(0)
    else:
        print(f"指令\"{command}\"不存在或不可用。")

def main():
    try:
        choice = "下载漫画" # 初始化预留位
    except Exception as err:
        print(f"初始化发生异常：{type(err).__name__}:{err}")
        traceback.print_exc()
        return
    print(f"欢迎使用 JMcomic Downloader！\n{text.TEXT['menu']}")
    while True:
        try:
            # 获取用户选择并执行
            choice = ui.select (message = "请选择操作：",
                                choices= text.MENU_SECTIONS,
                                default= choice)
            execute_command(choice)
        except Exception as err:
            print(f"\n程序发生异常：{type(err).__name__}:{err}\n")
            input("回车以查看详细报错...")
            traceback.print_exc()