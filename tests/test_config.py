"""Tests for the config module."""

from jmcomic_downloader.config import Configs, get_config


class TestConfigs:
    def test_default_values(self):
        cfg = Configs()
        assert cfg.show_jm_log is True
        assert cfg.current_style_name == "默认风格"

    def test_edit_and_read_back(self, tmp_path):
        cfg = Configs()
        cfg.config_file = str(tmp_path / "config.yml")
        result = cfg.edit("show_download_log", False)
        assert result is False

        import simpsave as ss

        assert ss.read("show_download_log", file=cfg.config_file) is False

    def test_reset_restores_defaults(self, tmp_path):
        cfg = Configs()
        cfg.config_file = str(tmp_path / "config.yml")
        cfg.edit("show_download_log", False)
        cfg.edit("current_style_name", "赛博霓虹")
        cfg.reset()
        assert cfg.show_jm_log is True
        assert cfg.current_style_name == "默认风格"

    def test_get_config_singleton(self):
        a = get_config()
        b = get_config()
        assert a is b

    def test_load_creates_config_when_missing(self, tmp_path):
        cfg = Configs()
        cfg.config_file = str(tmp_path / "config.yml")
        cfg.load()
        import simpsave as ss

        assert ss.has("config_exsist", file=cfg.config_file)

    def test_load_reads_existing_values(self, tmp_path):
        cfg = Configs()
        cfg.config_file = str(tmp_path / "config.yml")
        cfg.edit("show_download_log", False)
        cfg.edit("current_style_name", "粉红樱花")

        new_cfg = Configs()
        new_cfg.config_file = str(tmp_path / "config.yml")
        new_cfg.load()
        assert new_cfg.show_jm_log is False
        assert new_cfg.current_style_name == "粉红樱花"
