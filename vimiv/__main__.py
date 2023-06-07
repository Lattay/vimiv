#!/usr/bin/env python3
# vim: ft=python fileencoding=utf-8 sw=4 et sts=4
"""Vimiv executable."""
from .app import Vimiv


def main():
    import signal
    import sys

    signal.signal(signal.SIGINT, signal.SIG_DFL)  # ^C
    Vimiv().run(sys.argv)


if __name__ == "__main__":
    main()
