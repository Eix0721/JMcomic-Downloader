import InquirerPy
from InquirerPy import inquirer,utils
import libs.self.text as text


current_style = InquirerPy.get_style (text.INTERFACE_STYLES ["默认风格"], # type: ignore no att
                                      style_override = True)


def input_text (mesage) -> str:
    output_str = InquirerPy.inquirer.text(  # type: ignore
        message = mesage,
        style = current_style,
    ).execute()
    return output_str

def confirm (message) -> bool:
    choice = InquirerPy.inquirer.select(   # type: ignore
        message=message,
        choices=["确认","取消"],
        style = current_style,
        pointer = ">"
    ).execute()
    return choice == "确认"

def select (message,choices,default=None) -> str:
    choice = InquirerPy.inquirer.select(  # type: ignore
                message = message,
                choices = choices,
                default = default,
                style = current_style,
                pointer = ">"
            ).execute()
    return choice

def set_style() ->None:
    global current_style
    is_keep_going = True
    style_choice = "默认风格"
    
    while is_keep_going:
        try:
            style_choices = list(text.INTERFACE_STYLES.keys()) + ["取消"]
            style_choice = select ("请选择主题风格：",style_choices,
                                          default=style_choice)
            if style_choice == "取消":
                is_keep_going = False
                return
            style_args = text.INTERFACE_STYLES[style_choice]
            current_style = InquirerPy.get_style (style_args,style_override=True) # type: ignore
        except Exception as err:
            print(f"切换样式时发生错误：{type(err).__name__}:{err}")
            break