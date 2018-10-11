__all__ = ['KeyHolder']

import win32api
import win32con
import threading
from . import vkcode
from . import keyLocker


class KeyHolder(threading.Thread):
        def __init__(self):
                super().__init__()
                self.hold_lock = keyLocker.KeyLocker()

        def press(self, key: str):
                self.hold_lock.lock()
                win32api.keybd_event(vkcode.VK_CODE[key], 0, 0, 0)
                self.hold_lock.unlock()
                return

        def release(self, key: str):
                self.hold_lock.lock()
                win32api.keybd_event(vkcode.VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
                self.hold_lock.unlock()
                return
