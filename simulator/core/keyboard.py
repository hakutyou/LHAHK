__all__ = ['Keyboard']

from . import wait


class Keyboard:
        def __init__(self):
                pass

        def key_once(self, key: str, state: bool, hwnd=None):  # state = True 表示按下)
                pass    # 需要定义

        def lock(self):
                pass

        def unlock(self):
                pass

        def is_lock(self):
                return False

        def press(self, key, hwnd=None):
                self.key_once(key, True, hwnd)

        def release(self, key, hwnd=None):
                self.key_once(key, False, hwnd)

        def input_key(self, key, hwnd=None):
                self.press(key, hwnd)
                wait.random_wait()
                self.release(key, hwnd)

        def input_string(self, string, hwnd=None):
                probe = False
                for ch in string:
                        if probe:
                                wait.random_wait()
                        probe = True

                        self.press(ch, hwnd)
                        wait.random_wait()
                        self.release(ch)
