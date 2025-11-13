from ast import In
from ctypes import pointer


class link:
    jm = "https://github.com/hect0x7/JMComic-Crawler-Python"  # JMcomic
    yaml = "https://github.com/yaml/pyyaml"  # pyYAML
    InquirerPy = "https://github.com/kazhala/InquirerPy" # InquirerPy
    pj = "https://github.com/Eix0721/JMcomic-Downloader"
    

class text:
    menu = f"""
\n\n
--------------菜单----------------
详细菜单：显示此菜单页面
下载漫画：下载JMcomic漫画
设置选项：设置文件路径等（开发中）
切换主题：更改界面主题风格
关于项目：显示关于页面
退出程序：退出该程序
**↑/↓ - 选择 | ENTER - 确认
---------------------------------\n
"""

    settings = f"""
\n\n
--------------设置-------------
日志：关闭下载日志输出
**↑/↓ - 选择 | ENTER - 确认
------------------------------\n
"""

    about = f"""
\n\n
感谢您使用JMcomic Downloader！
本项目由Eix0721开发，遵循MIT开源许可证。
仓库地址：{link.pj}

本项目使用了以下第三方库：
**JMComic Crawler Python
描述：提供漫画下载核心功能
地址：{link.jm}
**pyYAML
描述：未来用于配置文件支持
地址：{link.yaml}
**InquirerPy
描述：构建交互式命令行界面
地址：{link.InquirerPy}

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
JMcomic 也是一款十分优秀的漫画软件，
关爱禁漫娘，请不要一次性下载过多本子!
"""
#TODO 调整数据结构
class infurce_style:
    all_styles = {
    "默认风格":{
    "questionmark": "#e5c07b",
    "answermark": "#e5c07b",
    "answer": "#61afef",
    "input": "#98c379",
    "question": "",
    "answered_question": "",
    "instruction": "#abb2bf",
    "long_instruction": "#abb2bf",
    "pointer": "#61afef",
    "checkbox": "#98c379",
    "separator": "",
    "skipped": "#5c6370",
    "validator": "",
    "marker": "#e5c07b",
    "fuzzy_prompt": "#c678dd",
    "fuzzy_info": "#abb2bf",
    "fuzzy_border": "#4b5263",
    "fuzzy_match": "#c678dd",
    "spinner_pattern": "#e5c07b",
    "spinner_text": "",
},
    "极简黑白":{
    "questionmark": "fg:#ffffff bold",   # 白色 ?
    "question":     "bold",              # 问题本身
    "answer":       "fg:#ffffff bold",   # 已选项
    "pointer":      "fg:#ffffff bold",   # 指针 >
    "highlighted":  "reverse",           # 反白
    "instruction":  "",                  # 提示文字
},
    "赛博朋克":{
    "questionmark": "fg:#00ffff bold",   # 青色 ?
    "question":     "fg:#ff00ff bold",   # 洋红问题
    "answer":       "fg:#39ff14 bold",   # 亮绿答案
    "pointer":      "fg:#ffaa00 bold",   # 橙黄指针
    "highlighted":  "fg:#ff00ff bold underline",
    "instruction":  "fg:#888888",
},
    "商务深蓝":{
    "questionmark": "fg:#0052cc bold",   # IBM 蓝
    "question":     "fg:#0052cc bold",
    "answer":       "fg:#36b37e bold",   # 成功绿
    "pointer":      "fg:#0052cc",
    "highlighted":  "fg:#ffffff bg:#0052cc",
    "instruction":  "fg:#6b778c",
}}