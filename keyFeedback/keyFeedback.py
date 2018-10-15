__all__ = ['PRESS_MAPPING', 'RELEASE_MAPPING', 'init']

import copy
from . import keyHolder
from .base import mapping
from .mapping import normal

PRESS_MAPPING = {}
RELEASE_MAPPING = {}

_key_holder = None


def init():
        global _key_holder, PRESS_MAPPING, RELEASE_MAPPING
        _key_holder = keyHolder.KeyHolder()
        mapping.init(_key_holder)
        PRESS_MAPPING = mapping.PRESS_MAPPING
        RELEASE_MAPPING = mapping.RELEASE_MAPPING
        mapping.mode_switch(normal.normalMapping)
        return _key_holder
