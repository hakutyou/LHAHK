__all__ = ['mapping']

from interactive.qmlReceive import qmlReceive
from interactive.setting import TRAY

from . import core
from .mode import base


class Mapping:
        def __init__(self):
                self._mode = ['']
                self._press_mapping = {}
                self._release_mapping = {}
                self._key_holder = core  # globalKeyboard.globalKeyboard

        @property
        def key_holder(self):
                return self._key_holder

        @property
        def mode(self):
                return self._mode[0]

        @property
        def press_mapping(self):
                return self._press_mapping

        @property
        def release_mapping(self):
                return self._release_mapping

        def mode_switch(self, mode: base.BaseMapping):
                self._mapping_switch(mode.MODE, mode.press(), mode.release())
                qmlReceive.refresh_keylist()

        def _mapping_switch(self, mode, press_mapping=None, release_mapping=None):
                self._key_holder.keyboardHwnd.lock()
                self._key_holder.keyboardGlob.lock()
                self._key_holder.keyboardGlob.release('Rshift')
                self._key_holder.keyboardGlob.release('Escape')
                self._mode[0] = mode
                if press_mapping is not None:
                        self._press_mapping.clear()
                        for i in press_mapping:
                                self._press_mapping[i] = press_mapping[i]
                if release_mapping is not None:
                        self._release_mapping.clear()
                        for i in release_mapping:
                                self._release_mapping[i] = release_mapping[i]
                self._key_holder.keyboardGlob.unlock()
                self._key_holder.keyboardHwnd.unlock()
                if TRAY:
                        qmlReceive.tray_info('MODE switch', mode)


mapping = Mapping()
