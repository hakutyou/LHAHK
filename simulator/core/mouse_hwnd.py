import win32api
import win32con

from . import mouse


class MouseHwnd(mouse.Mouse):
        def __init__(self):
                super().__init__()
                self.__OPERATE_MAPPING = {
                        'left': (win32con.WM_LBUTTONUP,         # 0, False
                                 win32con.WM_LBUTTONDOWN,       # 1, True
                                 win32con.WM_LBUTTONDBLCLK),    # 2
                        'middle': (win32con.WM_MBUTTONUP,       # 0, False
                                   win32con.WM_MBUTTONDOWN,     # 1, True
                                   win32con.WM_MBUTTONDBLCLK),  # 2
                        'right': (win32con.WM_RBUTTONUP,        # 0, False
                                  win32con.WM_RBUTTONDOWN,      # 1, True
                                  win32con.WM_RBUTTONDBLCLK)    # 2
                }
                self.__BUTTON_MAPPING = {
                        'left': win32con.MK_LBUTTON,
                        'middle': win32con.MK_MBUTTON,
                        'right': win32con.MK_RBUTTON,
                }

        def move_key_once(self, key: str, state: bool, x, y, hwnd=None, lock=False):
                if hwnd is None:
                        return False
                long_position = win32api.MAKELONG(x, y)
                try:
                        operate = self.__OPERATE_MAPPING[key][state]
                        button = self.__BUTTON_MAPPING[key]
                except TypeError:
                        operate = self.__OPERATE_MAPPING['left'][state]
                        button = self.__BUTTON_MAPPING['left']
                win32api.SendMessage(hwnd, operate, button, long_position)
