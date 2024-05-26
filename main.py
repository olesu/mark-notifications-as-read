from dataclasses import dataclass
import os
from typing import Callable
from github import Github, Auth
import sys


def version() -> None:
    print('mark_all_gh_notifications as read, version 0.1.0')


def mark_all_notifications_as_read() -> None:
    github_token = os.environ.get('GITHUB_TOKEN')
    if github_token is None:
        print('GITHUB_TOKEN is required')
        sys.exit(1)

    github = Github(Auth.Token(github_token))
    for notification in github.get_user().get_notifications():
        notification.mark_as_read()


@dataclass
class Context:
    version: Callable[[], None] = None
    mark_all_notifications_as_read: Callable[[], None] = None


context = Context()


def run():
    if len(sys.argv) > 1 and sys.argv[1] == '--version':
        context.version()
        return

    context.mark_all_notifications_as_read()


if __name__ == '__main__':
    context.version = version
    context.mark_all_notifications_as_read = mark_all_notifications_as_read
    run()
