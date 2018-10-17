__all__ = ['globalMouse']

import win32api
import win32con


class _GlobalMouse:
        def __init__(self):
                self.__OPERATE_MAPPING = {
                        'left': (win32con.MOUSEEVENTF_LEFTDOWN,
                                 win32con.MOUSEEVENTF_LEFTUP),
                        'middle': (win32con.MOUSEEVENTF_MIDDLEDOWN,
                                   win32con.MOUSEEVENTF_MIDDLEUP),
                        'right': (win32con.MOUSEEVENTF_RIGHTDOWN,
                                  win32con.MOUSEEVENTF_RIGHTUP),
                }

        @staticmethod
        def move(x, y):
                win32api.SetCursorPos((x, y))

        def key_once(self, key: str, state: bool):  # state = True 表示按下
                if state:
                        try:
                                operate = self.__OPERATE_MAPPING[key][0]
                        except KeyError:
                                operate = self.__OPERATE_MAPPING['left'][0]
                else:
                        try:
                                operate = self.__OPERATE_MAPPING[key][1]
                        except KeyError:
                                operate = self.__OPERATE_MAPPING['left'][1]
                win32api.mouse_event(operate, 0, 0, 0, 0)


globalMouse = _GlobalMouse()
