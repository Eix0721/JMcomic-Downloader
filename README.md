<div align="center">
   <img width="200" height="200" src="assets/icon.ico">
   <h1>JMComic Downloader</h1>
   <p>基于 Python 开发的命令行漫画下载工具，提供简洁易用的交互式界面，支持批量下载漫画等功能。</p>

[![Python](https://img.shields.io/badge/Python-3.9%2B-b)](https://www.python.org/)  [![Platform](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://github.com/Eix0721/JMcomic-Downloader/releases)  [![开源许可](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT) 

</div>

---

## ✨ 特性

<div align="center">

| 🚀 **快速开始** | 🎮 **交互友好** | 🎯 **批量下载** | 🎨 **多种主题**|
|:--------------:|:--------------:|:--------------:|:-------------:|
| 下载即用，无需配置 | 优雅的命令行界面 | 支持多个漫画ID |内置多种界面风格 |




</div>


## 🚀 快速开始

- ### **📦 推荐方式 - 即开即用**

1. **下载程序** 
   - 前往 [Release ](https://github.com/Eix0721/JMcomic-Downloader/releases)页面
   - 下载 `-win_amd64` 结尾的压缩包

2. **运行程序**
   ```bash
   解压后双击运行 "JMcomic Downloader.exe"
   ```

- ### 🛠️ 源码运行

1. **克隆项目**
   ```
   git clone https://github.com/Eix0721/JMcomic-Downloader.git
   cd JMcomic-Downloader\src
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行程序**
   ```bash
   python jmcomic_downloader.py
   ```



## 🎮 使用指南

- #### 主菜单

启动程序后，你将看到如下菜单：

```
--------------菜单--------------
详细菜单：显示此菜单页面
下载漫画：下载JMcomic漫画
设置选项：设置文件路径等（开发中）
切换主题：更改界面主题风格
关于项目：显示关于页面
退出程序：退出该程序
**↑/↓ - 选择 | ENTER - 确认
------------------------------
```

- #### 下载漫画

  - 使用方向键，选择`下载漫画`；
  - 输入禁漫车号（如：`350234`）；
    - 多个车号用空格分隔（如：`350234 114514 1919810`）；
  - 检查待下载漫画列表并确认下载；
  - 等待下载完成，漫画将分文件夹保存在本地。
- #### 关闭下载日志
  - 选择`设置选项`；
  - 选择`关闭下载日志输出`；
  - 已关闭下载日志输出。
    - 若要开启，再次选择`开启下载日志输出`即可。


## 📂 文件结构

```
JMComic-Downloader/
├── jmcomic_downloader.py    # 程序入口
├── libs/
│   ├── self/
│   │   ├── core.py          # 核心逻辑
│   │   ├── ui.py            # 界面交互
│   │   ├── text.py          # 文本内容
│   │   └── confit_manager.py # 配置管理
│   └── ...
├── README.md                # 项目说明
└── ...
```



## 🛠️ 技术栈&鸣谢
感谢以下开源项目：
<div align="center">

| 技术&模块 | 用途 | 推荐版本 |
|------|------|------|
| **[Python](https://www.python.org)** | 开发语言 | 3.9+ |
| **[JMComic Crawlern](https://github.com/hect0x7/JMComic-Crawler-Python)** | 漫画下载核心 | latest |
| **[InquirerPy](https://github.com/kazhala/InquirerPy)** | 交互式命令行 | latest |
| **[pyYAML](https://github.com/yaml/pyyaml)** | 配置文件支持 | latest |

</div>

- **关爱禁漫娘，请不要一次性下载过多本子!**



## 📜 开源协议

本项目采用 [MIT 许可证](https://github.com/Eix0721/JMcomic-Downloader?tab=MIT-1-ov-file) 开源。

> **版权所有 © 2025 Eix0721**

## 🔔 其他事项
本项目目前仍在**初步开发阶段**，计划逐步完善更多特性。  
本人是第一次开发项目，不论是对git的使用，还是commit、README、release，或是代码质量，都会有有诸多不妥，请谅解😥。

欢迎您提交 [Issue](https://github.com/Eix0721/JMcomic-Downloader/issues/new) 或 [PR](https://github.com/Eix0721/JMcomic-Downloader/compare) 参与改进！  

## ⭐Star History
<a href="https://www.star-history.com/#Eix0721/JMcomic-Downloader&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Eix0721/JMcomic-Downloader&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Eix0721/JMcomic-Downloader&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Eix0721/JMcomic-Downloader&type=date&legend=top-left" />
 </picture>
</a>
<div align="center">
如果这个项目对你有帮助，给个 ⭐Star⭐ 支持一下吧！
<div>
