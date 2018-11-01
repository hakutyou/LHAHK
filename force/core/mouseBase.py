# coding=utf-8

__all__ = ['MouseBase']

import general


class MouseBase(object):
        def __init__(self):
                pass

        def move_key_once(self, key: str, state: int, x, y, hwnd=None, lock=False) -> bool:
                return False

        def lock(self) -> None:
                pass

        def unlock(self) -> None:
                pass

        def mouse_down(self, key: str, x: int, y: int, hwnd=None) -> None:
                self.move_key_once(key, 1, x, y, hwnd)

        def mouse_up(self, key: str, x: int, y: int, hwnd=None) -> None:
                self.move_key_once(key, 0, x, y, hwnd)

        def click(self, key: str, x: int, y: int, hwnd=None, lock=False, wait_time=0.05) -> None:
                self.mouse_down(key, x, y, hwnd)
                if lock:
                        self.lock()
                general.random_wait(wait_time)
                if lock:
                        self.unlock()
                self.mouse_up(key, x, y, hwnd)

        def double_click(self, key: str, x: int, y: int, hwnd=None, lock=False) -> None:
                pass
