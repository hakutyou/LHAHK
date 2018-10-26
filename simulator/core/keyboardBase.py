__all__ = ['KeyboardBase']

import general


class KeyboardBase:
        def __init__(self):
                pass

        def key_once(self, key: str, state: bool, hwnd):  # state = True 表示按下)
                pass    # 需要定义

        def press(self, key, hwnd=None):
                self.key_once(key, True, hwnd)

        def release(self, key, hwnd=None):
                self.key_once(key, False, hwnd)

        def input_key(self, key, hwnd=None):
                self.press(key, hwnd)
                general.random_wait()
                self.release(key, hwnd)

        def input_string(self, string, hwnd=None):
                probe = False
                for ch in string:
                        if probe:
                                general.random_wait()
                        probe = True

                        self.press(ch, hwnd)
                        general.random_wait()
                        self.release(ch)
