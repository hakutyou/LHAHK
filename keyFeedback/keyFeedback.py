__all__ = ['PRESS_MAPPING', 'RELEASE_MAPPING', 'init']

import copy
from . import keyHolder

PRESS_MAPPING = {}
RELEASE_MAPPING = {}

_key_holder = None


def init():
        global PRESS_MAPPING, RELEASE_MAPPING, _key_holder
        PRESS_MAPPING = copy.deepcopy(press_mapping())
        RELEASE_MAPPING = copy.deepcopy(release_mapping())
        _key_holder = keyHolder.KeyHolder()
        return _key_holder


def print_window_title(window_name: str):
        print(window_name)


def reverse_window_title(window_name: str):
        print(window_name[::-1])


def switch_mapping(_press_mapping=None, _release_mapping=None):
        global PRESS_MAPPING, RELEASE_MAPPING
        _key_holder.hold_lock.lock()
        release_key('right_shift')
        if _press_mapping is not None:
                PRESS_MAPPING.clear()
                for i in _press_mapping:
                        PRESS_MAPPING[i] = _press_mapping[i]
        if _release_mapping is not None:
                RELEASE_MAPPING.clear()
                for i in _release_mapping:
                        RELEASE_MAPPING[i] = _release_mapping[i]
        _key_holder.hold_lock.unlock()


def hold_key(key: str, extra=0):
        print('hold')
        _key_holder.press(key, extra)


def release_key(key: str, extra=0):
        print('release')
        _key_holder.release(key, extra)


def press_mapping():
        return {
                "#['A']": print_window_title,
                "#['S']": lambda _: switch_mapping(press_mapping_ex()),
                "#['D']": lambda _: hold_key('left_win'),
                "#['Rshift', 'A']": lambda _: switch_mapping(press_mapping_numpad(),
                                                           release_mapping_numpad()),
        }


def press_mapping_ex():
        return {
                "#['A']": reverse_window_title,
                "#['S']": lambda _: switch_mapping(press_mapping()),
        }


def press_mapping_numpad():
        return {
                "*['Q']": lambda _: hold_key('numpad_7'),
                "*['W']": lambda _: hold_key('numpad_8'),
                "*['E']": lambda _: hold_key('numpad_9'),
                "*['A']": lambda _: hold_key('numpad_4'),
                "*['S']": lambda _: hold_key('numpad_5'),
                "*['D']": lambda _: hold_key('numpad_6'),
                "*['Z']": lambda _: hold_key('numpad_1'),
                "*['X']": lambda _: hold_key('numpad_2'),
                "*['C']": lambda _: hold_key('numpad_3'),
                "#['Rshift', 'A']": lambda _: switch_mapping(press_mapping(),
                                                           release_mapping()),
        }


def release_mapping_numpad():
        return {
                "*['Q']": lambda _: release_key('numpad_7'),
                "*['W']": lambda _: release_key('numpad_8'),
                "*['E']": lambda _: release_key('numpad_9'),
                "*['A']": lambda _: release_key('numpad_4'),
                "*['S']": lambda _: release_key('numpad_5'),
                "*['D']": lambda _: release_key('numpad_6'),
                "*['Z']": lambda _: release_key('numpad_1'),
                "*['X']": lambda _: release_key('numpad_2'),
                "*['C']": lambda _: release_key('numpad_3'),
        }


def release_mapping():
        return {
                "['D']": lambda _: release_key('left_win'),
        }
