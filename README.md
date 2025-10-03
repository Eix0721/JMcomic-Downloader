# JMcomic Downloader

一个基于 [JMComic Crawler Python](https://github.com/hect0x7/JMComic-Crawler-Python) 的简易命令行本子下载工具。  
本项目支持通过输入禁漫车号，批量下载漫画，并**计划支持**YAML 配置下载 与更多功能。  

---

## 📌 功能特性与未来计划
- [x] 支持输入单个或多个禁漫车号（以空格分隔）进行批量下载  
- [x] 自动检测并安装依赖模块（`jmcomic`、`pyYAML`）  
- [x] 关于页面
- [ ] 下载前显示漫画标题（待办）  
- [ ] YAML 文件配置（待办）  
- [ ] 更完整的设置功能（待办）  
- [ ] 无Python环境运行（待办）
---

## 🚀 安装与运行

### 1. 克隆仓库
```bash
git clone https://github.com/Eix0721/JMcomic-Downloader.git
cd JMcomic-Downloader
```

### 2. 安装依赖
每次运行时，脚本会自动检测当前解释器是否安装了依赖模块：  
- __ [JMComic Crawler Python](https://github.com/hect0x7/JMComic-Crawler-Python)__
- [pyYAML](https://github.com/yaml/pyyaml)  

如未安装，程序会提示是否同意自动安装。
如同意，将自动执行：
```bash
#{sys.excutable} 为当前Python解释器目录
#{moduleName} 为缺失的模块名
"{sys.executable}" -m pip install -q {moduleName}
```
您也可以手动安装依赖模块（`jmcomic`,`pyYAML`）:
```bash
pip install jmcomic
pip install pyyaml
```
### 3. 运行脚本
```bash
python JMdownloader.py
```

- 此外，您也可以手动下载 [main\JMdownloader.py](https://github.com/Eix0721/JMcomic-Downloader/blob/main/main/JMdownloader.py) 源文件快速运行

---

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

您可以输入 `2` → 再输入 `350234 350235`  
即可下载两个禁漫车对应的漫画。
目前，下载漫画会在所处目录中创建与漫画同名的文件，并将下载的漫画保存其中。此外，保存的格式为`.webp`，文件名为`<页数>.webp`。后续将支持更改保存格式、命名方式等功能

---

## 🙏 致谢

本项目使用以下开源项目：

- **[JMComic Crawler Python](https://github.com/hect0x7/JMComic-Crawler-Python)**  
  📖 提供漫画下载的核心功能  

- **[pyYAML](https://github.com/yaml/pyyaml)**  
  ⚙️ 未来将用于配置文件支持 

感谢以上项目的开发者与贡献者为开源社区作出的奉献！
###### - **此外 _JMcomic_ 也是一款十分优秀的漫画软件，关爱禁漫娘，请不要一次性下载过多本子！**
---

## 📌 项目状态
本项目目前仍在**初步开发阶段**，计划逐步完善 **配置功能、本子标题显示、YAML 配置支持** 等特性。  
欢迎提交 Issue 或 PR 参与改进！  
