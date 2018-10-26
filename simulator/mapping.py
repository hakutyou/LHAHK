__all__ = ['mapping']

import setting
import interactive

from . import core
from .mode import base


class Mapping:
        def __init__(self):
                self.__mode = ['']
                self.__press_mapping = {}
                self.__release_mapping = {}
                self.__key_holder = core.keyboard

        @property
        def key_holder(self):
                return self.__key_holder

        @property
        def mode(self):
                return self.__mode[0]

        @property
        def press_mapping(self):
                return self.__press_mapping

        @property
        def release_mapping(self):
                return self.__release_mapping

        def mode_switch(self, mode: base.BaseMapping, exit_action=None):
                if exit_action is not None:
                        exit_action(None)
                self.__mapping_switch(mode.MODE, mode.press(), mode.release())
                interactive.qmlCaller.refresh_keylist()

        def __mapping_switch(self, mode, press_mapping=None, release_mapping=None):
                self.__key_holder.lock()
                self.__key_holder.release('Rshift')
                self.__key_holder.release('Escape')
                self.__mode[0] = mode
                if press_mapping is not None:
                        self.__press_mapping.clear()
                        for i in press_mapping:
                                self.__press_mapping[i] = press_mapping[i]
                if release_mapping is not None:
                        self.__release_mapping.clear()
                        for i in release_mapping:
                                self.__release_mapping[i] = release_mapping[i]
                self.__key_holder.unlock()
                if setting.TRAY:
                        interactive.qmlCaller.tray_info('MODE switch', mode)


mapping = Mapping()
