import InquirerPy
from InquirerPy import inquirer, utils
import libs.self.text as text
from libs.self.config import CURRENT_STYLE_NAME,edit

# 当前界面风格，初始化为默认风格
current_style = InquirerPy.get_style(text.INTERFACE_STYLES[CURRENT_STYLE_NAME],  # type: ignore no att
                                     style_override=True)


def input_text(mesage) -> str:
    """
    显示文本输入提示框

    Args:
        mesage: 提示信息文本

    Returns:
        str: 用户输入的文本内容
    """
    output_str = InquirerPy.inquirer.text(  # type: ignore
        message=mesage,
        style=current_style,
    ).execute()
    return output_str


def confirm(message) -> bool:
    """
    显示确认对话框（是/否选择）

    Args:
        message: 确认提示信息

    Returns:
        bool: True表示用户选择"确认"，False表示选择"取消"
    """
    choice = InquirerPy.inquirer.select(   # type: ignore
        message=message,
        choices=["确认", "取消"],
        style=current_style,
        pointer=">"
            ).execute()
    return choice == "确认"


def select(message, choices, default=None) -> str:
    """
    显示选择菜单

    Args:
        message: 选择提示信息
        choices: 可选项列表
        default: 默认选中的选项

    Returns:
        str: 用户选择的选项文本
    """
    choice = InquirerPy.inquirer.select(  # type: ignore
        message=message,
        choices=choices,
        default=default,
        style=current_style,
        pointer=">"
    ).execute()
    return choice


def set_style() -> None:
    """
    交互式设置界面主题风格

    允许用户从预定义的风格列表中选择界面主题，
    支持循环选择直到用户取消或发生错误
    """
    global current_style,CURRENT_STYLE_NAME
    is_keep_going = True
    style_choice = "默认风格"  # 默认选中的风格
    
    while is_keep_going:
        try:
            # 构建风格选择列表，包含所有可用风格和取消选项
            style_choices = list(text.INTERFACE_STYLES.keys()) + ["取消"]

            # 显示风格选择菜单
            style_choice = select("请选择主题风格：", style_choices,
                                          default=style_choice)

            # 用户选择取消，退出设置
            if style_choice == "取消":
                is_keep_going = False
                return

            # 获取并存储选中的风格配置
            CURRENT_STYLE_NAME = edit("current_style_name",style_choice)
            style_args = text.INTERFACE_STYLES[style_choice]

            # 应用新风格
            current_style = InquirerPy.get_style(style_args, style_override=True)  # type: ignore

        except Exception as err:
            # 处理风格切换过程中的异常
            print(f"切换样式时发生错误：{type(err).__name__}:{err}")
            break