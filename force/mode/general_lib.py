# coding=utf-8

__all__ = ['switch_mode']

import force.core

from force.mapping import mapping


def switch_mode(mode, exit_action=None):
        return ('切换到 {0} 模式'.format(mode.MODE),
                lambda _: mapping.mode_switch(mode, exit_action))


def click(x, y, key='left', hwnd=None, wait=.1) -> None:
        if hwnd is None:
                force.core.mouse.click(key, x, y, hwnd, wait)
        else:
                force.core.mouseBack.click(key, x, y, hwnd, wait)


def input_key(key, hwnd) -> None:
        if hwnd is None:
                force.core.keyboard.input_key(key)
        else:
                force.core.keyboardBack.input_key(key, hwnd)
