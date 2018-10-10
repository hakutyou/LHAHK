__all__ = ['PRESS_MAPPING', 'RELEASE_MAPPING']

import copy
import win32api
import win32con
from . import vkcode


def print_window_title(window_name: str):
        print(window_name)


def reverse_window_title(window_name: str):
        print(window_name[::-1])


def hold_a_key(_: str):
        print('hold a key')
        win32api.keybd_event(vkcode.VK_CODE['q'], 0, 0, 0)


def release_a_key(_: str):
        print('release a key')
        win32api.keybd_event(vkcode.VK_CODE['q'], 0, win32con.KEYEVENTF_KEYUP, 0)


def switch_mapping(new_mapping):
        global PRESS_MAPPING
        PRESS_MAPPING.clear()
        for i in new_mapping:
                PRESS_MAPPING[i] = new_mapping[i]


class KeyFeedback:
        def __init__(self, debug=False):
                self.debug = debug

                global PRESS_MAPPING, RELEASE_MAPPING
                self.MAPPING1 = {"['A']": print_window_title,
                                 "['S']": lambda _: switch_mapping(self.MAPPING2),
                                 "['D']": hold_a_key}
                self.MAPPING2 = {"['A']": reverse_window_title,
                                 "['S']": lambda _: switch_mapping(self.MAPPING1)}
                self.REMAPPING1 = {"['D']": release_a_key}

                PRESS_MAPPING = copy.deepcopy(self.MAPPING1)
                RELEASE_MAPPING = copy.deepcopy(self.REMAPPING1)


PRESS_MAPPING = {}
RELEASE_MAPPING = {}

if __name__ == '__main__':
        import threading

        keyFeedback = KeyFeedback()
        t = threading.Thread(target=keyFeedback.MAPPING1["['A']"], args=("test",))
        t.start()
