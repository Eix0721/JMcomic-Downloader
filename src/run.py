#!/usr/bin/env python3
"""启动入口 — 在 uv 未同步时可直接 python src/run.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jmcomic_downloader import main

if __name__ == "__main__":
    main()
