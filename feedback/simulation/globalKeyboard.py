__all__ = ['globalKeyboard']

import win32api
import win32con

from . import vkcode
from . import keyLocker


class _GlobalKeyboard:
        def __init__(self):
                self.hold_lock = keyLocker.KeyLocker()

        def key_once(self, key: str, state: bool):  # state = True 表示按下
                virtual_code = vkcode.VK_CODE[key]
                scan_code = vkcode.scan_code(virtual_code)
                if state:
                        operate = 0
                else:
                        operate = win32con.KEYEVENTF_KEYUP
                self.hold_lock.lock()
                win32api.keybd_event(virtual_code, scan_code, operate, 0)
                self.hold_lock.unlock()
                return True


globalKeyboard = _GlobalKeyboard()
