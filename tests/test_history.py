"""Tests for the history module."""

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

    def test_add_record_uses_provided_values(self):
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

    def test_get_history_singleton(self):
        a = get_history()
        b = get_history()
        assert a is b

    def test_print_history_does_not_raise(self, capsys):
        h = DownloadHistory()
        h.add({"id": "42", "title": "测试", "author": "某作者"})
        h.print_history()
        captured = capsys.readouterr()
        assert "42" in captured.out
        assert "测试" in captured.out
