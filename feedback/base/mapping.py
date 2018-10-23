__all__ = ['mode_switch', 'init', 'MODE', 'PRESS_MAPPING', 'RELEASE_MAPPING']

from ..mapping import base
from .. import simulation
from ..refresh import refresh

_key_holder = None
MODE = ['']
PRESS_MAPPING = {}
RELEASE_MAPPING = {}


def init(key_holder):
        global _key_holder
        _key_holder = key_holder


def mode_switch(mode: base.BaseMapping):
        mapping_switch(mode.MODE, mode.press(), mode.release())
        refresh()


def mapping_switch(_mode, _press_mapping=None, _release_mapping=None):
        global PRESS_MAPPING, RELEASE_MAPPING
        _key_holder.hold_lock().lock()
        simulation.release('Rshift')
        simulation.release('Escape')
        MODE[0] = _mode
        if _press_mapping is not None:
                PRESS_MAPPING.clear()
                for i in _press_mapping:
                        PRESS_MAPPING[i] = _press_mapping[i]
        if _release_mapping is not None:
                RELEASE_MAPPING.clear()
                for i in _release_mapping:
                        RELEASE_MAPPING[i] = _release_mapping[i]
        _key_holder.hold_lock().unlock()
