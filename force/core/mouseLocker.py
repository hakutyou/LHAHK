# coding=utf-8

__all__ = ['MouseLocker']

from ctypes import *


class MouseLocker(object):
        def __init__(self):
                pass

        @staticmethod
        def lock() -> None:
                windll.user32.BlockInput(True)   # it works as admin

        @staticmethod
        def unlock() -> None:
                windll.user32.BlockInput(False)  # it works as admin
