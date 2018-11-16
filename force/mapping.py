# coding=utf-8

__all__ = ['get_macs', 'set_macs',
           'key_holder', 'get_mode', 'press_mapping', 'release_mapping',
           'mode_switch']

import setting
import dmail

from . import core

__mode = ['']
__macs = [0x00]
__press_mapping = {}
__release_mapping = {}
__key_holder = core.keyboard
__mouse_holder = core.mouse


def get_macs() -> int:
        return __macs[0]


def set_macs(value: int) -> None:
        __macs[0] = value


def key_holder():
        return __key_holder


def get_mode() -> str:
        return __mode[0]


def press_mapping() -> dict:
        return __press_mapping


def release_mapping() -> dict:
        return __release_mapping


def mode_switch(mode, exit_action=None) -> None:
        def __mapping_switch(_mode, press=None, release=None):
                set_macs(0x00)
                __key_holder.lock()
                __key_holder.release('Rshift')
                __key_holder.release('Escape')
                __mode[0] = _mode
                if press is not None:
                        __press_mapping.clear()
                        for i in press:
                                __press_mapping[i] = press[i]
                if release is not None:
                        __release_mapping.clear()
                        for i in release:
                                __release_mapping[i] = release[i]
                __key_holder.unlock()
                if setting.TRAY:
                        dmail.qmlCaller.tray_info('MODE switch', _mode)

        if exit_action is not None:
                exit_action(None)
        __mapping_switch(mode.MODE, mode.press(), mode.release())
        dmail.qmlCaller.refresh_keylist()
