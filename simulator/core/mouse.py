__all__ = ['Mouse']

from . import wait
from . import mouseLocker


class Mouse:
        def __init__(self, locker=False):
                if locker:
                        self.locker = mouseLocker.MouseLocker()
                pass

        def move_key_once(self, key: str, state: int, x, y, hwnd=None, lock=True):
                self.move(x, y)
                if lock:
                        self.lock()
                wait.random_wait()
                if lock:
                        self.unlock()
                self.key_once(key, state)
                return

        def move(self, x, y):
                pass

        def key_once(self, key: str, state: int):
                pass

        def lock(self):
                self.locker.lock()

        def unlock(self):
                self.locker.unlock()

        def mouse_down(self, key, x, y, hwnd=None):
                self.move_key_once(key, True, x, y, hwnd)

        def mouse_up(self, key, x, y, hwnd=None):
                self.move_key_once(key, False, x, y, hwnd)

        def click(self, key, x, y, hwnd=None, lock=True, wait_time=0.05):
                if (hwnd is None) and lock:
                        self.lock()
                self.mouse_down(key, x, y, hwnd)
                if wait_time > 0.05:
                        wait.random_wait(wait_time)
                self.mouse_up(key, x, y, hwnd)
                if (hwnd is None) and lock:
                        self.unlock()
                return

        def double_click(self, key, x, y, hwnd=None, lock=True):
                if hwnd is None:
                        if lock:
                                self.lock()
                        self.click(key, x, y, hwnd, False)
                        wait.random_wait()
                        self.click(key, x, y, hwnd, False)
                        if lock:
                                self.unlock()
                else:
                        __double_click = 2
                        self.move_key_once(key, __double_click, x, y, hwnd)
