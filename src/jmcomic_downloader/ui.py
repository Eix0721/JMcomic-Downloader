from typing import Any

import InquirerPy
from InquirerPy import inquirer

from . import text
from .config import cfgs

_current_style: Any = None


def _get_style() -> Any:
    global _current_style
    if _current_style is not None:
        return _current_style

    if cfgs.current_style_name not in text.INTERFACE_STYLES:
        print("所选主题不存在，已修改为默认风格。")
        cfgs.current_style_name = "默认风格"

    _current_style = InquirerPy.get_style(
        text.INTERFACE_STYLES[cfgs.current_style_name],
        style_override=True,
    )
    return _current_style


def input_text(message: str) -> str:
    return inquirer.text(message=message, style=_get_style()).execute()


def confirm(message: str) -> bool:
    choice = inquirer.select(
        message=message,
        choices=["确认", "取消"],
        style=_get_style(),
        pointer=">",
    ).execute()
    return choice == "确认"


def select(message: str, choices: list[str], default: str | None = None) -> str:
    choice = inquirer.select(
        message=message,
        choices=choices,
        default=default,
        style=_get_style(),
        pointer=">",
    ).execute()
    return choice


def set_style() -> None:
    global _current_style
    style_choice = "默认风格"

    while True:
        try:
            style_choices = list(text.INTERFACE_STYLES.keys()) + ["取消"]
            style_choice = select("请选择主题风格：", style_choices, default=style_choice)

            if style_choice == "取消":
                return

            cfgs.current_style_name = cfgs.edit("current_style_name", style_choice)
            style_args = text.INTERFACE_STYLES[style_choice]
            _current_style = InquirerPy.get_style(style_args, style_override=True)

        except Exception as err:
            print(f"切换样式时发生错误：{type(err).__name__}:{err}")
            break
