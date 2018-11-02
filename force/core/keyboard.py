# coding=utf-8

__all__ = ['key_once',
           'press', 'release',
           'input_key', 'input_string',
           'is_lock']

import win32api
import win32con
import exception
import general
from . import vkcode

_locker = [0]


@exception.general_exception(False)
def key_once(key: str, down: bool, hwnd=None) -> None:  # down = True 表示按下
        virtual_code = vkcode.VK_CODE[key]
        scan_code = vkcode.scan_code(virtual_code)

        if hwnd is None:
                if down:
                        operate = 0
                else:
                        operate = win32con.KEYEVENTF_KEYUP
                lock()
                win32api.keybd_event(virtual_code, scan_code, operate, 0)
                unlock()
        else:
                if down:
                        operate = win32con.WM_KEYDOWN
                        code = scan_code << 16 | 0x00000001
                else:
                        operate = win32con.WM_KEYUP
                        code = scan_code << 16 | 0xc0000001

                win32api.PostMessage(hwnd, operate, virtual_code, code)
        return


def lock() -> None:
        if _locker is not None:
                _locker[0] += 1


def unlock() -> None:
        if _locker is not None:
                _locker[0] -= 1


def is_lock() -> bool:  # 锁定时不触发 keyboardReceive
        if _locker is None:
                return False
        return _locker[0] > 0


def press(key, hwnd=None) -> None:
        key_once(key, True, hwnd)


def release(key, hwnd=None) -> None:
        key_once(key, False, hwnd)


def input_key(key, hwnd=None) -> None:
        press(key, hwnd)
        general.random_wait()
        release(key, hwnd)


def input_string(string, hwnd=None) -> None:
        probe = False
        for ch in string:
                if probe:
                        general.random_wait()
                probe = True

                press(ch, hwnd)
                general.random_wait()
                release(ch)
