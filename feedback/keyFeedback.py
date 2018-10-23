__all__ = ['MODE', 'PRESS_MAPPING', 'RELEASE_MAPPING', 'init']

from . import simulation
from .base import mapping
from .mapping import normal

MODE = None
PRESS_MAPPING = None
RELEASE_MAPPING = None

_key_holder = None


def init():
        global _key_holder, MODE, PRESS_MAPPING, RELEASE_MAPPING
        _key_holder = simulation  # globalKeyboard.globalKeyboard
        mapping.init(_key_holder)
        MODE = mapping.MODE
        PRESS_MAPPING = mapping.PRESS_MAPPING
        RELEASE_MAPPING = mapping.RELEASE_MAPPING
        mapping.mode_switch(normal.normalMapping)
        return _key_holder
