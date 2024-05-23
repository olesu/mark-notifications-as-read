import main
from contextlib import redirect_stdout
from io import StringIO


def test_mark_all_gh_notifications_as_read():
    buffer = StringIO()
    with redirect_stdout(buffer):
        main.run()

    assert buffer.getvalue().strip() == 'mark 1\nmark 2'
