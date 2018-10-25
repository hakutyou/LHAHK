import win32api
import win32con

from . import vkcode
from . import keyboard


class KeyboardGlob(keyboard.Keyboard):
        def __init__(self):
                super().__init__()
                self._locker = [0]

        def key_once(self, key: str, state: bool, hwnd=None):
                virtual_code = vkcode.VK_CODE[key]
                scan_code = vkcode.scan_code(virtual_code)
                if state:
                        operate = 0
                else:
                        operate = win32con.KEYEVENTF_KEYUP
                self.lock()
                win32api.keybd_event(virtual_code, scan_code, operate, 0)
                self.unlock()
                return True

        def lock(self):
                if self._locker is not None:
                        self._locker[0] += 1

        def unlock(self):
                if self._locker is not None:
                        self._locker[0] -= 1

        def is_lock(self):              # 锁定时不触发 keyboardReceive
                if self._locker is None:
                        return False
                return self._locker[0] > 0
