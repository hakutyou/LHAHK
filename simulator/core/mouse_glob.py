import win32con
import win32api

from . import mouse


class MouseGlob(mouse.Mouse):
        def __init__(self):
                super().__init__()
                self.__OPERATE_MAPPING = {
                        'left': (win32con.MOUSEEVENTF_LEFTUP,          # 0, False
                                 win32con.MOUSEEVENTF_LEFTDOWN),       # 1, True
                        'middle': (win32con.MOUSEEVENTF_MIDDLEUP,      # 0, False
                                   win32con.MOUSEEVENTF_MIDDLEDOWN),   # 1, True
                        'right': (win32con.MOUSEEVENTF_RIGHTUP,        # 0, False
                                  win32con.MOUSEEVENTF_RIGHTDOWN),     # 1, True
                }

        def move(self, x, y):
                win32api.SetCursorPos((x, y))

        def key_once(self, key, state):  # state = True(1) 表示按下
                try:
                        operate = self.__OPERATE_MAPPING[key][state]
                except TypeError:
                        operate = self.__OPERATE_MAPPING['left'][state]
                win32api.mouse_event(operate, 0, 0, 0, 0)
