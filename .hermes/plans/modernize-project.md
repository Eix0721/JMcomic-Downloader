# Modernize Project Plan

> **Goal:** Bring JMcomic-Downloader from "working but bare" to "standard modern Python project" — ruff formatting, type safety, test coverage, CI.

**Architecture:** No structural changes. Add dev tooling (ruff, mypy, pytest) as uv dev dependencies. Add type annotations to all function signatures. Write tests for the testable core (config, history, text — anything without network I/O or InquirerPy). Update the existing CI workflow to use uv and run quality gates.

**Tech Stack additions:** ruff, mypy, pytest, pre-commit

---

## Task 1: Add dev dependencies + pyproject.toml metadata

**Objective:** Add ruff, mypy, pytest as dev dependencies. Add classifiers, URLs, and pytest config to pyproject.toml.

**Files:**
- Modify: `pyproject.toml`

**Complete pyproject.toml:**

```toml
[project]
name = "jmcomic-downloader"
version = "1.0.0"
description = "基于 Python 开发的命令行漫画下载工具"
readme = "README.md"
license = { text = "MIT" }
authors = [
    { name = "Eix0721" },
]
requires-python = ">=3.10"
dependencies = [
    "jmcomic",
    "InquirerPy",
    "PyYAML",
    "simpsave",
]

[project.urls]
Homepage = "https://github.com/Eix0721/JMcomic-Downloader"
Repository = "https://github.com/Eix0721/JMcomic-Downloader"
Issues = "https://github.com/Eix0721/JMcomic-Downloader/issues"

[project.classifiers]
  "Development Status :: 4 - Beta",
  "Environment :: Console",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Topic :: Internet :: WWW/HTTP",
  "Topic :: Multimedia :: Graphics",

[project.scripts]
jmcomic-downloader = "jmcomic_downloader:main"

[project.optional-dependencies]
dev = [
    "ruff>=0.11",
    "mypy>=1.15",
    "pytest>=8.0",
    "pytest-env>=1.0",
]

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]
include = ["jmcomic_downloader*"]

[tool.uv]
package = true

[tool.ruff]
target-version = "py310"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "W", "UP"]

[tool.ruff.format]
quote-style = "double"

[tool.mypy]
python_version = "3.10"
strict = true
exclude = [
    "src/jmcomic_downloader/test_domain.py",
    "src/jmcomic_downloader/ui.py",
]
[[tool.mypy.overrides]]
module = "jmcomic.*"
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = "InquirerPy.*"
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = "simpsave"
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = "curl_cffi.*"
ignore_missing_imports = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

**Install:**

```bash
uv sync --group dev
```

**Verify:**

```bash
uv run ruff --version
uv run mypy --version
uv run pytest --version
```

Expected: three version strings, no errors.

**Commit:**

```bash
git add pyproject.toml uv.lock
git commit -m "build: add dev tooling (ruff, mypy, pytest) and pyproject metadata"
```

---

## Task 2: Format all source files with ruff

**Objective:** Auto-fix all formatting/lint issues across `src/jmcomic_downloader/`.

**Files:**
- Modify: all `src/jmcomic_downloader/*.py`

**Steps:**

```bash
uv run ruff check src/jmcomic_downloader/ --fix
uv run ruff format src/jmcomic_downloader/
```

**Check remaining issues:**

```bash
uv run ruff check src/jmcomic_downloader/
```

If any warnings remain (beyond ones we explicitly choose to leave), fix them manually.

**Commit:**

```bash
git add src/jmcomic_downloader/
git commit -m "style: apply ruff formatting and lint fixes"
```

---

## Task 3: Add type annotations to all function signatures

**Objective:** Every function/method in the package gets full type annotations.

**Scope:** All 6 files under `src/jmcomic_downloader/`.

**Complete annotated files:**

### `src/jmcomic_downloader/text.py` (annotations only — few changes needed)

```python
from .config import cfgs


def show_status(arg: bool) -> str:
    return "开启" if arg else "关闭"


def get_sections(orig_text: str) -> list[str]:
    sections: list[str] = []
    for line in orig_text.splitlines():
        line = line.strip()
        if "：" in line:
            section = line.split("：", 1)[0]
            sections.append(section)
    return sections


LINK: dict[str, str] = { ... }  # unchanged
TEXT: dict[str, str] = { ... }  # unchanged
INTERFACE_STYLES: dict[str, dict[str, str]] = { ... }  # unchanged
MENU_SECTIONS: list[str] = get_sections(TEXT["menu"])
SETTING_SECTIONS: list[str] = get_sections(TEXT["settings"])
```

### `src/jmcomic_downloader/config.py`

Changes needed:
- `edit(self, key: str, val: Any) -> Any` — add `Any` import
- `_defaults()` return type should be `dict[str, bool | str]`
- `get_config()` return type already there

### `src/jmcomic_downloader/core.py`

Changes needed:
- `jmcomic_download() -> None`
- `setting() -> None`
- `execute_command(command: str) -> None`
- `main() -> None`
- `execute_detail(arg: Any) -> dict[str, Any]` — `arg` is jmcomic album detail

### `src/jmcomic_downloader/history.py`

Changes needed:
- `add(self, details: dict[str, Any]) -> dict[str, Any]`
- `print_history(self) -> None`
- `get_latest(self) -> dict[str, Any] | None`
- `get_recent(self, limit: int = 10) -> list[dict[str, Any]]`
- `clear_all(self) -> None`
- `load(self) -> None`

### `src/jmcomic_downloader/ui.py`

Changes needed:
- `_get_style() -> InquirerPy.style.Style` (or just `-> Any` to avoid InquirerPy type hell)
- `input_text(message: str) -> str`
- `confirm(message: str) -> bool`
- `select(message: str, choices: list[str], default: str | None = None) -> str`
- `set_style() -> None`

### `src/jmcomic_downloader/test_domain.py`

Changes needed:
- `get_all_domain() -> set[str]`
- `test_domain(domain: str) -> None`
- `test_all_domains() -> None`

**Verify with mypy:**

```bash
uv run mypy src/jmcomic_downloader/
```

Expected: Success, no issues.

**Commit:**

```bash
git add src/jmcomic_downloader/
git commit -m "types: add type annotations to all function signatures"
```

---

## Task 4: Write tests for config module

**Objective:** Full test coverage for `Configs` class (load, edit, reset, save_all).

**Files:**
- Create: `tests/test_config.py`

**Test plan:**

1. `test_default_values` — Configs() sets correct defaults
2. `test_edit_and_read_back` — edit a key, verify it persists via simpsave
3. `test_reset_restores_defaults` — reset clears to defaults
4. `test_get_config_singleton` — get_config() returns same instance
5. `test_load_from_file` — write a yml manually, load it

**Note:** These tests need a temp directory and env var to control config file path. Since Configs hardcodes `_get_config_path()`, we'll mock `ss` functions with `monkeypatch`.

```python
import pytest
from jmcomic_downloader.config import Configs, get_config


class TestConfigs:
    def test_default_values(self):
        cfg = Configs()
        assert cfg.show_jm_log is True
        assert cfg.current_style_name == "默认风格"

    def test_edit_updates_value(self, monkeypatch, tmp_path):
        cfg = Configs()
        cfg.config_file = str(tmp_path / "config.yml")
        
        # ss.write 和 ss.read 走真实文件，但路径在 tmp_path
        result = cfg.edit("show_download_log", False)
        assert result is False
        assert cfg.show_jm_log is True  # edit doesn't mutate instance
        
        # 验证文件确实写了
        import simpsave as ss
        assert ss.read("show_download_log", file=cfg.config_file) is False

    def test_reset_restores_defaults(self, monkeypatch, tmp_path):
        cfg = Configs()
        cfg.config_file = str(tmp_path / "config.yml")
        cfg.edit("show_download_log", False)
        cfg.reset()
        assert cfg.show_jm_log is True
        assert cfg.current_style_name == "默认风格"

    def test_get_config_singleton(self):
        a = get_config()
        b = get_config()
        assert a is b
```

**Run:**

```bash
uv run pytest tests/ -v
```

Expected: ~5 passed.

**Commit:**

```bash
git add tests/test_config.py
git commit -m "test: add config module tests"
```

---

## Task 5: Write tests for history module

**Objective:** Test `DownloadHistory` add/get/clear/print without file I/O side effects.

**Files:**
- Create: `tests/test_history.py`

**Test plan:**

1. `test_empty_history` — freshly created history is empty
2. `test_add_record` — add returns record with expected keys
3. `test_get_latest` — returns most recent record
4. `test_get_recent` — respects limit
5. `test_clear_all` — clears all records
6. `test_print_history` — doesn't throw (smoke test)

```python
import pytest
from jmcomic_downloader.history import DownloadHistory, get_history


class TestDownloadHistory:
    def test_empty_history(self):
        h = DownloadHistory()
        assert h.total_downloads == []
        assert h.get_latest() is None

    def test_add_record(self):
        h = DownloadHistory()
        detail = {"id": "12345", "title": "测试本子", "author": "测试作者"}
        record = h.add(detail)
        assert record["jm_id"] == "12345"
        assert record["title"] == "测试本子"
        assert record["author"] == "测试作者"
        assert "download_time" in record

    def test_get_latest(self):
        h = DownloadHistory()
        h.add({"id": "1", "title": "A", "author": "X"})
        h.add({"id": "2", "title": "B", "author": "Y"})
        latest = h.get_latest()
        assert latest["jm_id"] == "2"

    def test_get_recent_limit(self):
        h = DownloadHistory()
        for i in range(5):
            h.add({"id": str(i), "title": f"N{i}", "author": "T"})
        recent = h.get_recent(limit=2)
        assert len(recent) == 2
        assert recent[0]["jm_id"] == "3"
        assert recent[1]["jm_id"] == "4"

    def test_clear_all(self):
        h = DownloadHistory()
        h.add({"id": "1", "title": "A", "author": "X"})
        h.clear_all()
        assert h.total_downloads == []

    def test_print_history_does_not_raise(self, capsys):
        h = DownloadHistory()
        h.add({"id": "42", "title": "测试", "author": "某作者"})
        h.print_history()
        captured = capsys.readouterr()
        assert "42" in captured.out
        assert "测试" in captured.out
```

**Run:**

```bash
uv run pytest tests/ -v
```

Expected: all tests from both test_config.py and test_history.py pass.

**Commit:**

```bash
git add tests/test_history.py
git commit -m "test: add history module tests"
```

---

## Task 6: Write tests for text module

**Objective:** Test pure functions in text.py (show_status, get_sections).

**Files:**
- Create: `tests/test_text.py`

**Test plan:**

1. `test_show_status_on` — True → "开启"
2. `test_show_status_off` — False → "关闭"
3. `test_get_sections_extracts_prefix` — "功能说明：xxx" → ["功能说明"]
4. `test_get_sections_skips_lines_without_colon` — lines without "：" are skipped
5. `test_menu_sections_is_populated` — MENU_SECTIONS is non-empty
6. `test_setting_sections_is_populated` — SETTING_SECTIONS is non-empty

```python
from jmcomic_downloader import text


class TestShowStatus:
    def test_on(self):
        assert text.show_status(True) == "开启"

    def test_off(self):
        assert text.show_status(False) == "关闭"


class TestGetSections:
    def test_extracts_prefix(self):
        result = text.get_sections("功能说明：显示此功能说明页面")
        assert result == ["功能说明"]

    def test_skips_lines_without_colon(self):
        result = text.get_sections("没有冒号的行\n有冒号：的内容")
        assert result == ["有冒号"]

    def test_menu_sections_populated(self):
        assert len(text.MENU_SECTIONS) > 0
        assert "下载漫画" in text.MENU_SECTIONS

    def test_setting_sections_populated(self):
        assert len(text.SETTING_SECTIONS) > 0
        assert "设置说明" in text.SETTING_SECTIONS
```

**Run:**

```bash
uv run pytest tests/ -v
```

Expected: all pass.

**Commit:**

```bash
git add tests/test_text.py
git commit -m "test: add text module tests"
```

---

## Task 7: Update CI workflow (pre-release.yml)

**Objective:** Switch from pip + requirements.txt to uv. Add quality gates (ruff, mypy, pytest) before the build step. Fix the PyInstaller entry point to match new package structure.

**Files:**
- Modify: `.github/workflows/pre-release.yml`

**Key changes:**
1. Install uv in CI, use `uv sync --group dev`
2. Add `ruff check`, `mypy`, `pytest` steps before PyInstaller
3. Fix PyInstaller spec: entry point is now `run.py` or `jmcomic_downloader/__main__.py` (module mode)
   - Best approach: `pyinstaller --onefile --console ... -m jmcomic_downloader` (module mode)
4. Remove `pip install -r src/requirements.txt` (no longer exists)

**Complete workflow:**

```yaml
name: pre_release

on:
  push:
    tags:
      - 'v[0-9]+.[0-9]+.[0-9]+'

jobs:
  quality:
    runs-on: windows-latest
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Install uv
      uses: astral-sh/setup-uv@v5
      with:
        enable-cache: true

    - name: Set up Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: Install dependencies
      run: uv sync --group dev

    - name: Lint with ruff
      run: uv run ruff check src/

    - name: Type check with mypy
      run: uv run mypy src/jmcomic_downloader/

    - name: Test with pytest
      run: uv run pytest tests/ -v

  build-windows:
    runs-on: windows-latest
    needs: quality
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0

    - name: Install uv
      uses: astral-sh/setup-uv@v5
      with:
        enable-cache: true

    - name: Set up Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"

    - name: Install dependencies
      run: uv sync

    - name: Install PyInstaller
      run: uv pip install pyinstaller

    - name: Prepare build environment
      shell: pwsh
      run: |
        if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
        if (Test-Path "dist") { Remove-Item -Recurse -Force "dist" }

    - name: Build with PyInstaller (module mode)
      shell: pwsh
      run: |
        uv run pyinstaller `
          --onefile --console `
          --name "JMcomic Downloader" `
          --icon="assets/icon.ico" `
          --hidden-import "jmcomic" `
          --hidden-import "InquirerPy" `
          --hidden-import "simpsave" `
          --hidden-import "yaml" `
          --paths "src" `
          -m jmcomic_downloader

    - name: Test the executable
      shell: pwsh
      run: |
        $fileSize = (Get-Item "dist/JMcomic Downloader.exe").Length
        Write-Host "Executable size: $fileSize bytes"
        if ($fileSize -gt 1000000) {
          Write-Host "Build appears to be successful"
          exit 0
        } else {
          Write-Host "Warning: Executable file size seems too small"
          exit 1
        }

    - name: Upload Build Artifact
      uses: actions/upload-artifact@v4
      with:
        name: JMcomic-Downloader-${{ github.ref_name }}
        path: dist/JMcomic Downloader.exe
        retention-days: 7
```

**Commit:**

```bash
git add .github/workflows/pre-release.yml
git commit -m "ci: migrate to uv, add quality gates (ruff/mypy/pytest)"
```

---

## Task 8 (Optional): Add pre-commit config

**Objective:** Auto-run ruff on every `git commit` so nothing slips through.

**Files:**
- Create: `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

**Install:**

```bash
uv run pre-commit install
```

**Commit:**

```bash
git add .pre-commit-config.yaml
git commit -m "chore: add pre-commit config with ruff"
```

---

## Risks & Open Questions

1. **mypy strict mode on ui.py** — InquirerPy doesn't ship types. We already excluded it in pyproject.toml. If mypy still complains about imports, add `ignore_missing_imports = true` for InquirerPy there.

2. **PyInstaller module mode** — The CI change switches from `jmcomic_downloader.py` entry to `-m jmcomic_downloader`. This needs `--paths src` so the package is findable. Tag-based CI won't fire until we push a tag — can't test until then.

3. **mypy and the `| None` syntax** — Python 3.10 supports `X | None` in type hints, so no `Optional` import needed. But `_cfgs: Configs | None = None` will make mypy strict happy.

4. **simpsave doesn't ship types** — We already added `ignore_missing_imports` override for it.

5. **test_domain.py has module-level network calls** (`option = JmOption.default()`, `disable_jm_log()`) — excluded from mypy due to import trickiness. Tests would need heavy mocking, so skip for now — it's not worth the effort for a test-only utility.
