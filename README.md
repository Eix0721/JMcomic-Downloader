
<div align="center">
    <img width="200" height="200" src="assets/icon.ico">
</div>
<div align="center">
    <h1>JMcomic Downloader</h1>
</div>
<div align="left">
<p>基于 Python 开发的命令行漫画下载工具，提供简洁易用的交互式界面，支持批量下载漫画等功能。</p>
</div>

---

## 📌 功能特性与未来计划
- [x] 支持输入单个或多个禁漫车号（以空格分隔）进行批量下载  
- [x] 自动检测并安装依赖模块（`pre-0.2.2`后已取消[#Commit10c4446](https://github.com/Eix0721/JMcomic-Downloader/commit/10c4446773b0aac7092a72878492769022679078)）
- [x] 关于及鸣谢页面
- [x] 无Python环境运行（可在[release](https://github.com/Eix0721/JMcomic-Downloader/releases)中下载`.exe`文件）
- [x] 隐藏下载日志
- [x] 代码结构、风格、可读性优化，文件结构优化
- [x] 基于[InquirerPY](#-致谢)的交互式命令行界面
- [ ] 下载前显示漫画标题、章节等信息
- [ ] YAML 文件配置（下载路径、存储格式、指定章节等）
- [ ] 更完整的设置功能
- [ ] GUI界面（远期目标，可能使用KivyMD）
- [ ] 跨平台支持（MacOS、Linux甚至Android）



## 🚀 安装与运行
### 🛵即开即用 ***（推荐）***：
下载`-win_amd64`结尾的[压缩文件](https://github.com/Eix0721/JMcomic-Downloader/releases)，解压后双击运行JMcomic Downloader.exe，即可快速使用。
### 🚲脚本运行：
##### 1. 克隆仓库或下载压缩包
克隆仓库
```bash
git clone https://github.com/Eix0721/JMcomic-Downloader.git
cd JMcomic-Downloader
```
或 下载`-Py3`结尾的[压缩包](https://github.com/Eix0721/JMcomic-Downloader/releases)（`pre-0.2.2`以前）
##### 2. 安装依赖
> `pre-0.2.2`及以后版本可忽略此内容

运行Python脚本时，会自动检测当前解释器是否已安装第三方依赖模块：  
- [JMComic](https://github.com/hect0x7/JMComic-Crawler-Python)
- [pyYAML](https://github.com/yaml/pyyaml)  

如未安装，程序会提示是否同意自动安装。
同意安装，将自动执行：
```python
#{sys.excutable} 为当前Python解释器目录
#{moduleName} 为缺失的模块名
os.system (f"\"{sys.executable}\" -m pip install -q {moduleName}")
```
如安装失败，请尝试手动安装上述模块。

#### 3. 运行脚本
```bash
python jmcomic_downloader.py
```


## 🕹️ 使用方法

运行后会显示菜单：

```
------------------菜单------------------
1.菜单：显示此菜单页面
2.下载：下载JMcomic漫画
        ╰批量下载以空格分割多个禁漫车
3.设置：设置文件路径等（开发中）
4.关于：显示关于页面
5.检测：检测非内置模块是否导入
        ╰目前检测 jmcomic, pyYAML 模块
6.退出：退出程序
----------------------------------------
```

#### 如何下载漫画？
输入 `2` 并回车以使用下载功能，输入禁漫车（如 `350234` ）并回车即可开始下载。
若要一次性下载多本漫画可使用空格分隔禁漫车（如 `350234 114514 1919810`）
漫画下载完成后，程序会在运行目录下创建一个与漫画同名的文件夹，并将所有下载内容保存于此。所有图片均以 `.webp` 格式存储，文件名为 `<页码>.webp`。后续将支持自定义保存格式和命名。



## 🙏 致谢

本项目使用以下开源项目：

- **[JMComic Crawler Python](https://github.com/hect0x7/JMComic-Crawler-Python)**  
  提供漫画下载的核心功能  

- **[pyYAML](https://github.com/yaml/pyyaml)**  
  未来将用于配置文件的支持

- **[InquirerPY](https://github.com/kazhala/InquirerPy)**
  用于构建交互式命令行界面

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
> **__JMcomic__ 是一款十分优秀的漫画软件，关爱禁漫娘，请不要一次性下载过多本子!**


## 🔔 其他事项
本项目目前仍在**初步开发阶段**，计划逐步完善[更多特性](#-功能特性与未来计划)。  
本人是第一次开发项目，不论是对git的使用，还是commit、README、release，或是代码质量，都会有有诸多不妥，请谅解😥。

欢迎提交 [Issue](https://github.com/Eix0721/JMcomic-Downloader/issues/new) 或 [PR](https://github.com/Eix0721/JMcomic-Downloader/compare) 参与改进！  

## ⭐Star History
<a href="https://www.star-history.com/#Eix0721/JMcomic-Downloader&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Eix0721/JMcomic-Downloader&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Eix0721/JMcomic-Downloader&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Eix0721/JMcomic-Downloader&type=date&legend=top-left" />
 </picture>
</a>

---

> 本项目采用 [MIT 许可证](https://github.com/Eix0721/JMcomic-Downloader?tab=MIT-1-ov-file) 开源。  
版权所有 © 2025  Eix0721