# coding=utf-8

__all__ = ['MouseReal']

import win32con
import win32api
import general

from . import mouseBase
from . import mouseLocker


class MouseReal(mouseBase.MouseBase):
        def __init__(self):
                super(__class__, self).__init__()
                self.locker = mouseLocker.MouseLocker()
                self.__OPERATE_MAPPING = {
                        'left': (win32con.MOUSEEVENTF_LEFTUP,          # 0, False
                                 win32con.MOUSEEVENTF_LEFTDOWN),       # 1, True
                        'middle': (win32con.MOUSEEVENTF_MIDDLEUP,      # 0, False
                                   win32con.MOUSEEVENTF_MIDDLEDOWN),   # 1, True
                        'right': (win32con.MOUSEEVENTF_RIGHTUP,        # 0, False
                                  win32con.MOUSEEVENTF_RIGHTDOWN),     # 1, True
                }

        def move_key_once(self, key: str, state: int, x, y, hwnd=None, lock=True):
                self.move(x, y)
                if lock:
                        self.lock()
                general.random_wait()
                if lock:
                        self.unlock()
                self.key_once(key, state)

        @staticmethod
        def move(x, y):
                win32api.SetCursorPos((x, y))

        def key_once(self, key, state):  # state = True(1) 表示按下
                try:
                        operate = self.__OPERATE_MAPPING[key][state]
                except TypeError:
                        operate = self.__OPERATE_MAPPING['left'][state]
                win32api.mouse_event(operate, 0, 0, 0, 0)

        def double_click(self, key, x, y, hwnd=None, lock=True):
                if lock:
                        self.lock()
                self.click(key, x, y, hwnd, False)
                general.random_wait()
                self.click(key, x, y, hwnd, False)
                if lock:
                        self.unlock()

        def lock(self):
                self.locker.lock()

        def unlock(self):
                self.locker.unlock()
