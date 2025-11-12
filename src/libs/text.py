from ast import In


class link:
    jm = "https://github.com/hect0x7/JMComic-Crawler-Python"  # JMcomic
    yaml = "https://github.com/yaml/pyyaml"  # pyYAML
    InquirerPy = "https://github.com/kazhala/InquirerPy" # InquirerPy
    pj = "https://github.com/Eix0721/JMcomic-Downloader"
    

class text:
    menu = f"""
\n\n{"-" * 18}菜单{"-" * 18}
1.菜单：显示此菜单页面
2.下载：下载JMcomic漫画
    ╰以空格分割多个禁漫车以批量下载
3.设置：设置文件路径等（开发中）
4.关于：显示关于页面
5.退出：退出程序
**输入数字以使用相关功能\n{"-" * 40}\n
    """

    settings = f"""
\n\n{"-" * 18}设置{"-" * 18}
1.日志：关闭下载日志输出
**输入数字以使用相关功能\n{"-" * 40}\n
"""

    about = f"""
\n\n感谢您使用JMcomic Downloader！本项目由Eix0721开发
仓库地址：{link.pj}

本项目使用了以下第三方库：
**JMComic Crawler Python
描述：提供漫画下载的核心功能
地址：{link.jm}
**pyYAML
描述：未来将用于配置文件支持
地址：{link.yaml}
**InquirerPy
描述：用于构建交互式命令行界面
地址：{link.InquirerPy}

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
JMcomic 也是一款十分优秀的漫画软件，关爱禁漫娘，请不要一次性下载过多本子!
"""
