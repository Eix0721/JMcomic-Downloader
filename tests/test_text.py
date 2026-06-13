"""Tests for the text module."""

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


class TestSections:
    def test_menu_sections_populated(self):
        assert len(text.MENU_SECTIONS) > 0
        assert "下载漫画" in text.MENU_SECTIONS

    def test_setting_sections_populated(self):
        assert len(text.SETTING_SECTIONS) > 0
        assert "设置说明" in text.SETTING_SECTIONS
