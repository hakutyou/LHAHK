__all__ = ['input_key', 'input_string', 'press', 'release', 'random_wait',
           'hold_lock']

import random
import time

from . import globalKeyboard
from . import handleKeyboard


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


def input_key(key, hwnd=None):
        press(key, hwnd)
        time.sleep(random_wait())
        release(key, hwnd)
        return


def input_string(string, hwnd=None):
        for ch in string:
                press(ch, hwnd)
                time.sleep(random_wait())
                release(ch)
                time.sleep(random_wait())
        return


def random_wait(interval=0.1, deviation=0.05):
        return 2 * random.random() * deviation - deviation + interval


def hold_lock():
        return globalKeyboard.globalKeyboard.hold_lock
