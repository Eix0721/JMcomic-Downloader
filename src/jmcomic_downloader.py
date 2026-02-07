# Copyright (c) 2025 Eix0721
# Licensed under the MIT License. See LICENSE file in the project root for full license information.

import os
import sys

# 添加项目根目录到 Python 路径，确保打包后能正确导入
if getattr(sys, 'frozen', False):
    # 如果是打包后的可执行文件
    application_path = os.path.dirname(sys.executable)
    # 添加可执行文件所在目录到路径
    if application_path not in sys.path:
        sys.path.insert(0, application_path)
else:
    # 如果是源码运行
    src_dir = os.path.dirname(os.path.abspath(__file__))
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)

from libs.self.core import main

if __name__ == "__main__":
    main()
