import sys


def version():
    print('mark_all_gh_notifications as read, version 0.1.0')


def run():
    if len(sys.argv) > 1 and sys.argv[1] == '--version':
        version()
        return

    print('mark 1')
    print('mark 2')


if __name__ == '__main__':
    run()
