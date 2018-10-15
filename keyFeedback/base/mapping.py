__all__ = ['mode_switch', 'init', 'PRESS_MAPPING', 'RELEASE_MAPPING']

from . import key
from ..mapping import base

_key_holder = None
PRESS_MAPPING = {}
RELEASE_MAPPING = {}


def init(key_holder):
        global _key_holder
        _key_holder = key_holder
        key.init(_key_holder)


def mode_switch(mode: base.BaseMapping):
        mapping_switch(mode.press(), mode.release())


def mapping_switch(_press_mapping=None, _release_mapping=None):
        global PRESS_MAPPING, RELEASE_MAPPING
        _key_holder.hold_lock.lock()
        key.release('right_shift')
        if _press_mapping is not None:
                PRESS_MAPPING.clear()
                for i in _press_mapping:
                        PRESS_MAPPING[i] = _press_mapping[i]
        if _release_mapping is not None:
                RELEASE_MAPPING.clear()
                for i in _release_mapping:
                        RELEASE_MAPPING[i] = _release_mapping[i]
        _key_holder.hold_lock.unlock()
