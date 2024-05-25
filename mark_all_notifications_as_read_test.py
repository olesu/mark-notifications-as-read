import main


def test_mark_all_notifications_as_read():
    was_called = {}

    def mark_all_notifications_as_read_fake():
        was_called['mark_all_notifications_as_read_fake'] = True

    main.mark_all_notifications_as_read(mark_all_notifications_as_read_fake)

    assert was_called['mark_all_notifications_as_read_fake']
