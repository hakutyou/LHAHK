# coding=utf-8

__all__ = ['real_key_once', 'real_move', 'real_move_key_once', 'move_key_once',
           'mouse_up', 'mouse_down', 'real_mouse_up', 'real_mouse_down',
           'real_click', 'click', 'real_double_click', 'double_click']

import win32api
import win32con
from ctypes import *  # windll
import exception
import general

__REAL_OPERATE_MAPPING = {
        'left': (win32con.MOUSEEVENTF_LEFTUP,  # 0, False
                 win32con.MOUSEEVENTF_LEFTDOWN),  # 1, True
        'middle': (win32con.MOUSEEVENTF_MIDDLEUP,  # 0, False
                   win32con.MOUSEEVENTF_MIDDLEDOWN),  # 1, True
        'right': (win32con.MOUSEEVENTF_RIGHTUP,  # 0, False
                  win32con.MOUSEEVENTF_RIGHTDOWN),  # 1, True
}

__HWND_OPERATE_MAPPING = {
        'left': (win32con.WM_LBUTTONUP,  # 0, False
                 win32con.WM_LBUTTONDOWN,  # 1, True
                 win32con.WM_LBUTTONDBLCLK),  # 2
        'middle': (win32con.WM_MBUTTONUP,  # 0, False
                   win32con.WM_MBUTTONDOWN,  # 1, True
                   win32con.WM_MBUTTONDBLCLK),  # 2
        'right': (win32con.WM_RBUTTONUP,  # 0, False
                  win32con.WM_RBUTTONDOWN,  # 1, True
                  win32con.WM_RBUTTONDBLCLK)  # 2
}
__HWND_BUTTON_MAPPING = {
        'left': win32con.MK_LBUTTON,
        'middle': win32con.MK_MBUTTON,
        'right': win32con.MK_RBUTTON,
}


def real_key_once(key: str, state: int) -> None:
        operate = __REAL_OPERATE_MAPPING[key][state]
        win32api.mouse_event(operate, 0, 0, 0, 0)


def real_move(x: int, y: int) -> None:
        win32api.SetCursorPos((x, y))


def real_move_key_once(key: str, state: int, x: int, y: int, lock: bool = False) -> bool:
        real_move(x, y)
        if lock:
                real_lock()
                general.random_wait()
        if lock:
                real_unlock()
        real_key_once(key, state)
        return True


@exception.general_exception(False)
def move_key_once(key: str, state: int, x: int, y: int, hwnd=None, lock: bool = False) -> bool:
        def hwnd_move_key_once() -> bool:
                long_position = win32api.MAKELONG(x, y)
                try:
                        operate = __HWND_OPERATE_MAPPING[key][state]
                        button = __HWND_BUTTON_MAPPING[key]
                except TypeError:
                        raise exception.ObjectException('just left middle right accepted')
                win32api.SendMessage(hwnd, operate, button, long_position)
                return True

        if hwnd is None:
                return real_move_key_once(key, state, x, y, lock)
        else:
                return hwnd_move_key_once()


def real_lock() -> None:
        windll.user32.BlockInput(True)  # it works as admin


def real_unlock() -> None:
        windll.user32.BlockInput(False)  # it works as admin


def mouse_down(key: str, x: int, y: int, hwnd=None, lock=False) -> None:
        move_key_once(key, 1, x, y, hwnd, lock)


def mouse_up(key: str, x: int, y: int, hwnd=None, lock=False) -> None:
        move_key_once(key, 0, x, y, hwnd, lock)


def real_mouse_down(key: str) -> None:
        real_key_once(key, 1)


def real_mouse_up(key: str) -> None:
        real_key_once(key, 0)


def click(key: str, x: int, y: int, hwnd=None, lock=False, wait_time=0.05) -> None:
        if hwnd is None:
                real_move(x, y)
                real_click(key, lock, wait_time)
        else:
                mouse_down(key, x, y, hwnd)
                general.random_wait(wait_time)
                mouse_up(key, x, y, hwnd)


def real_click(key: str, lock=False, wait_time=0.05) -> None:
        real_mouse_down(key)
        if lock:
                real_lock()
        general.random_wait(wait_time)
        if lock:
                real_unlock()
        real_mouse_up(key)


def double_click(key: str, x: int, y: int, hwnd=None, lock=False) -> None:
        def hwnd_double_click():
                db_click = 2
                move_key_once(key, db_click, x, y, hwnd)

        if hwnd is None:
                real_move(x, y)
                real_double_click(key, lock)
        else:
                hwnd_double_click()


def real_double_click(key: str, lock=False) -> None:
        real_click(key, lock)
        if lock:
                real_lock()
        general.random_wait()
        if lock:
                real_unlock()
        real_click(key, lock)
