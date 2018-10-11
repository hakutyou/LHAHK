__all__ = ['PRESS_MAPPING', 'RELEASE_MAPPING', 'locker']

import copy
from . import keyHolder

key_holder = keyHolder.KeyHolder()
PRESS_MAPPING = {}
RELEASE_MAPPING = {}


def print_window_title(window_name: str):
        print(window_name)


def reverse_window_title(window_name: str):
        print(window_name[::-1])


def hold_a_key(_: str):
        print('hold a key')
        key_holder.press('q')


def release_a_key(_: str):
        print('release a key')
        key_holder.release('q')


def switch_mapping(new_mapping):
        global PRESS_MAPPING
        PRESS_MAPPING.clear()
        for i in new_mapping:
                PRESS_MAPPING[i] = new_mapping[i]


class KeyFeedback:
        def __init__(self, debug=False):
                self.debug = debug

                global PRESS_MAPPING, RELEASE_MAPPING
                self.MAPPING1 = {"#['A']": print_window_title,
                                 "#['S']": lambda _: switch_mapping(self.MAPPING2),
                                 "['D']": hold_a_key}
                self.MAPPING2 = {"#['A']": reverse_window_title,
                                 "#['S']": lambda _: switch_mapping(self.MAPPING1)}
                self.REMAPPING1 = {"['D']": release_a_key}

                PRESS_MAPPING = copy.deepcopy(self.MAPPING1)
                RELEASE_MAPPING = copy.deepcopy(self.REMAPPING1)


locker = key_holder.hold_lock

if __name__ == '__main__':
        import threading

        keyFeedback = KeyFeedback()
        t = threading.Thread(target=keyFeedback.MAPPING1["['A']"], args=("test",))
        t.start()
