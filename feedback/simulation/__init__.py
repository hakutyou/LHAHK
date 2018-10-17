__all__ = ['input_key', 'input_string', 'press', 'release', 'random_wait',
           'hold_lock',
           'move', 'mouse_down', 'mouse_up', 'click']

import random
import time

from . import globalKeyboard
from . import handleKeyboard
from . import globalMouse


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


def move(x, y, hwnd=None):
        if hwnd is None:
                globalMouse.globalMouse.move(x, y)
        else:
                pass
        return


def mouse_down(key, hwnd=None):
        if hwnd is None:
                globalMouse.globalMouse.key_once(key, True)
        else:
                pass
        return


def mouse_up(key, hwnd=None):
        if hwnd is None:
                globalMouse.globalMouse.key_once(key, False)
        else:
                pass
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


def click(key, hwnd=None):
        mouse_down(key, hwnd)
        random_wait()
        mouse_up(key, hwnd)
        return


def random_wait(interval=0.1, deviation=0.05):
        time.sleep(2 * random.random() * deviation - deviation + interval)


def hold_lock():
        return globalKeyboard.globalKeyboard.hold_lock
