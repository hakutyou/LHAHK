# coding=utf-8

__all__ = ['mapping']

import setting
import dmail


from . import core
from .mode import base


class Mapping:
        def __init__(self):
                self.__mode = ['']
                self.__macs = [0x00]
                self.__press_mapping = {}
                self.__release_mapping = {}
                self.__key_holder = core.keyboard
                self.__mouse_holder = core.mouse

        def get_macs(self) -> int:
                return self.__macs[0]

        def set_macs(self, value: int) -> None:
                self.__macs[0] = value

        @property
        def key_holder(self):
                return self.__key_holder

        @property
        def mode(self) -> str:
                return self.__mode[0]

        @property
        def press_mapping(self) -> dict:
                return self.__press_mapping

        @property
        def release_mapping(self) -> dict:
                return self.__release_mapping

        def mode_switch(self, mode: base.BaseMapping, exit_action=None) -> None:
                def __mapping_switch(_mode, press_mapping=None, release_mapping=None):
                        self.set_macs(0x00)
                        self.__key_holder.lock()
                        self.__key_holder.release('Rshift')
                        self.__key_holder.release('Escape')
                        self.__mode[0] = _mode
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
                                dmail.qmlCaller.tray_info('MODE switch', _mode)

                if exit_action is not None:
                        exit_action(None)
                __mapping_switch(mode.MODE, mode.press, mode.release)
                dmail.qmlCaller.refresh_keylist()


mapping = Mapping()
