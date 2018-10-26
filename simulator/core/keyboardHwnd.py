__all__ = ['KeyboardHwnd']

import win32api
import win32con

from . import keyboardBase
from . import vkcode


class KeyboardHwnd(keyboardBase.KeyboardBase):
        def __init__(self):
                super().__init__()

        def key_once(self, key: str, state: bool, hwnd=None):  # state = True 表示按下
                if hwnd is None:
                        return False
                virtual_code = vkcode.VK_CODE[key]
                scan_code = vkcode.scan_code(virtual_code)
                if state:
                        operate = win32con.WM_KEYDOWN
                        code = scan_code << 16 | 0x00000001
                else:
                        operate = win32con.WM_KEYUP
                        code = scan_code << 16 | 0xc0000001

                win32api.PostMessage(hwnd, operate, virtual_code, code)
                return True
