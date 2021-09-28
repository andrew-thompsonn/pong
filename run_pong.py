#!/usr/bin/env python

from pong_window import PongWindow
from pong_engine import PongEngine


def main():
    window = PongWindow()
    engine = PongEngine(window)


if __name__ == "__main__":
    main()
