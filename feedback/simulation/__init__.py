__all__ = ['input_key', 'input_string', 'press', 'release', 'random_wait',
           'hold_lock',
           'mouse_down', 'mouse_up', 'click', 'double_click']

import random
import time

from . import globalKeyboard
from . import handleKeyboard
from . import globalMouse
from . import handleMouse
from . import mouseLocker


def press(key, hwnd=None):
        if hwnd is None:
                globalKeyboard.globalKeyboard.key_once(key, True)
        else:
                handleKeyboard.handleKeyboard.key_once(key, True, hwnd)
        return


def release(key, hwnd=None):
        if hwnd is None:
                globalKeyboard.globalKeyboard.key_once(key, False)
        else:
                handleKeyboard.handleKeyboard.key_once(key, False, hwnd)
        return


def mouse_down(key, x, y, hwnd=None):
        if hwnd is None:
                globalMouse.globalMouse.move(x, y)
                mouseLocker.mouseLocker.lock()
                random_wait()
                mouseLocker.mouseLocker.unlock()
                globalMouse.globalMouse.key_once(key, True)
        else:
                handleMouse.handleMouse.move_key_once(key, True, x, y, hwnd)

        return


def mouse_up(key, x, y, hwnd=None):
        if hwnd is None:
                globalMouse.globalMouse.move(x, y)
                mouseLocker.mouseLocker.lock()
                random_wait()
                mouseLocker.mouseLocker.unlock()
                globalMouse.globalMouse.key_once(key, False)
        else:
                handleMouse.handleMouse.move_key_once(key, False, x, y, hwnd)
        return


def input_key(key, hwnd=None):
        press(key, hwnd)
        random_wait()
        release(key, hwnd)
        return


def input_string(string, hwnd=None):
        probe = False
        for ch in string:
                if probe:
                        random_wait()
                probe = True

                press(ch, hwnd)
                random_wait()
                release(ch)
        return


def click(key, x, y, hwnd=None):
        mouse_down(key, x, y, hwnd)
        mouseLocker.mouseLocker.lock()
        random_wait()
        mouseLocker.mouseLocker.unlock()
        mouse_up(key, x, y, hwnd)
        return


def double_click(key, x, y, hwnd=None):
        if hwnd is None:
                click(key, x, y)
                mouseLocker.mouseLocker.lock()
                random_wait()
                mouseLocker.mouseLocker.unlock()
                click(key, x, y)
        else:
                __double_click = 2
                handleMouse.handleMouse.move_key_once(
                        key, __double_click, x, y, hwnd)


def random_wait(interval=0.05, deviation=0.025):
        time.sleep(2 * random.random() * deviation - deviation + interval)


def hold_lock():
        return globalKeyboard.globalKeyboard.hold_lock
