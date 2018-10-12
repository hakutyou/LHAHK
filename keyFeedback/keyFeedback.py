__all__ = ['PRESS_MAPPING', 'RELEASE_MAPPING', 'key_holder', 'KeyFeedback']

import copy
from . import keyHolder


PRESS_MAPPING = {}
RELEASE_MAPPING = {}
key_holder = keyHolder.KeyHolder()


def print_window_title(window_name: str):
        print(window_name)


def reverse_window_title(window_name: str):
        print(window_name[::-1])


def switch_mapping(new_mapping):
        global PRESS_MAPPING
        PRESS_MAPPING.clear()
        for i in new_mapping:
                PRESS_MAPPING[i] = new_mapping[i]


class KeyFeedback:
        def __init__(self, debug=False):
                self.debug = debug

                # self.locker = self.key_holder.hold_lock

                global PRESS_MAPPING, RELEASE_MAPPING

                PRESS_MAPPING = copy.deepcopy(MAPPING1)
                RELEASE_MAPPING = copy.deepcopy(REMAPPING1)


def hold_a_key(_: str):
        print('hold a key')
        key_holder.press('q')


def release_a_key(_: str):
        print('release a key')
        key_holder.release('q')


MAPPING1 = {"#['A']": print_window_title,
            "#['S']": lambda _: switch_mapping(MAPPING2),
            "['D']": hold_a_key}
MAPPING2 = {"#['A']": reverse_window_title,
            "#['S']": lambda _: switch_mapping(MAPPING1)}
REMAPPING1 = {"['D']": release_a_key}

if __name__ == '__main__':
        import threading

        keyFeedback = KeyFeedback()
        t = threading.Thread(target=MAPPING1["['A']"], args=("test",))
        t.start()
