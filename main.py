import sys


def version():
    print('mark_all_gh_notifications as read, version 0.1.0')


def mark_all_notifications_as_read_adapter():
    print('mark 1')
    print('mark 2')


def mark_all_notifications_as_read(mark_all_notifications_as_read_adapter):
    mark_all_notifications_as_read_adapter()


def run():
    if len(sys.argv) > 1 and sys.argv[1] == '--version':
        version()
        return

    mark_all_notifications_as_read(mark_all_notifications_as_read_adapter)


if __name__ == '__main__':
    run()
