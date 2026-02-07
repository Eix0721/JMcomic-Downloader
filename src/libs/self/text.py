from libs.self.config import cfgs

def showing_satus(arg) ->str:
    return "开启" if arg else "关闭"

def get_sections (orig_text) ->list[str]:
    sections = []
    for line in orig_text.splitlines():
            line = line.strip()
            if "：" in line:
                section = line.split("：", 1)[0]
                sections.append(section)
    return sections

LINK = {
    "jm": "https://github.com/hect0x7/JMComic-Crawler-Python",  # JMcomic
    "yaml": "https://github.com/yaml/pyyaml",                   # pyYAML
    "InquirerPy": "https://github.com/kazhala/InquirerPy",      # InquirerPy
    "SimpSave": "https://github.com/Water-Run/SimpSave",        # SimpSave
    "pj": "https://github.com/Eix0721/JMcomic-Downloader"       # 项目地址
}


TEXT = {
    "menu": f"""
\n\n
{"功能":-^36}
功能说明：显示此功能说明页面
下载漫画：下载JMcomic漫画
设置选项：设置文件路径等（开发中）
历史记录：查看下载历史记录
关于项目：显示关于页面
退出程序：退出该程序
**↑/↓ - 选择 | ENTER - 确认
{"":-^36}\n
""",

    "settings": f"""\n
{"设置":-^36}
设置说明：显示该设置说明页
{showing_satus(not cfgs.SHOW_JM_LOG)}下载日志输出：开关下载日志输出
切换主题：更改界面主题风格
测试连接：检测当前IP可访问的Jmcomic域名（测试功能，暂不准确）
恢复默认：重置所有设置为默认值
退出设置：返回主菜单
**↑/↓ - 选择 | ENTER - 确认
{"":-^36}\n
""",

    "about": f"""\n
感谢您使用JMcomic Downloader！
本项目由Eix0721开发，遵循MIT开源许可证。
仓库地址：{LINK['pj']}

本项目使用了以下第三方库：
**JMComic Crawler Python
描述：提供漫画下载核心功能
地址：{LINK['jm']}
**SimpSave
描述：配置文件读写工具
地址：{LINK['SimpSave']}
**InquirerPy
描述：构建交互式命令行界面
地址：{LINK['InquirerPy']}

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
JMcomic 也是一款十分优秀的漫画软件，
关爱禁漫娘，请不要一次性下载过多本子~
\n
"""
}



# --- 界面风格配置 ---
INTERFACE_STYLES = {
    "默认风格": {
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
    "商务深蓝": {
        "questionmark": "fg:#0052cc bold",
        "question": "fg:#0052cc bold",
        "answer": "fg:#36b37e bold",
        "pointer": "fg:#0052cc",
        "highlighted": "fg:#ffffff bg:#0052cc",
        "instruction": "fg:#6b778c",
    },
    "粉红樱花": {
        "questionmark": "fg:#ff9eb5 bold",
        "question": "fg:#ff6f91 bold",
        "answer": "fg:#ffb7c5 bold",
        "input": "fg:#ff8fab",
        "pointer": "fg:#ff6f91 bold",
        "highlighted": "fg:#ffffff bg:#ff9eb5",
        "instruction": "fg:#c97b8f",
        "separator": "fg:#ffd6e0",
    },
    "赛博霓虹": {
        "questionmark": "fg:#00ffff bold",
        "question": "fg:#ff00ff bold",
        "answer": "fg:#39ff14 bold",
        "input": "fg:#00ff9c",
        "pointer": "fg:#ffaa00 bold",
        "highlighted": "fg:#000000 bg:#ff00ff",
        "instruction": "fg:#7a7a7a",
        "separator": "fg:#444444",
    },
    "绿色森林": {
        "questionmark": "fg:#6fbf73 bold",
        "question": "fg:#4f8f52 bold",
        "answer": "fg:#7ecf8b bold",
        "input": "fg:#5fae6a",
        "pointer": "fg:#4f8f52",
        "highlighted": "fg:#1e1e1e bg:#7ecf8b",
        "instruction": "fg:#8fae94",
        "separator": "fg:#3f5f45",
    },
    "碧蓝海色": {
        "questionmark": "fg:#4fc3f7 bold",
        "question": "fg:#0288d1 bold",
        "answer": "fg:#81d4fa bold",
        "input": "fg:#4fc3f7",
        "pointer": "fg:#0288d1 bold",
        "highlighted": "fg:#ffffff bg:#01579b",
        "instruction": "fg:#90a4ae",
        "separator": "fg:#37474f",
    },
    "薰衣草紫": {
        "questionmark": "fg:#c792ea bold",
        "question": "fg:#b39ddb bold",
        "answer": "fg:#d1b3ff bold",
        "input": "fg:#c792ea",
        "pointer": "fg:#b39ddb",
        "highlighted": "fg:#1e1e1e bg:#c792ea",
        "instruction": "fg:#a0a0c0",
        "separator": "fg:#4a4458",
    }
}


MENU_SECTIONS = get_sections(TEXT["menu"])
SETTING_SECTIONS = get_sections(TEXT["settings"])