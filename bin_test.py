import subprocess


def test_show_version():
    output = subprocess.run(
        ["python3", "main.py", "--version"],
        capture_output=True,
        text=True,
        check=True
    )
    assert output.stdout == 'mark_all_gh_notifications as read, version 0.1.0\n'
