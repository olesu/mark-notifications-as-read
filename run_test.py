import sys
import main
from contextlib import redirect_stdout
from io import StringIO


def test_show_version(monkeypatch):
    expected = 'a version string'

    monkeypatch.setattr(sys, 'argv', ['main.py', '--version'])
    monkeypatch.setattr(main.context, 'version', lambda: print(expected))

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.run()

    assert buffer.getvalue().strip() == expected


def test_mark_all_gh_notifications_as_read(monkeypatch):
    expected = 'mark 1\nmark 2'

    monkeypatch.setattr(
        main.context,
        "mark_all_notifications_as_read",
        lambda: print(expected))

    buffer = StringIO()
    with redirect_stdout(buffer):
        main.run()

    assert buffer.getvalue().strip() == expected
