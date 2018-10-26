__all__ = ['switch_mode']

import simulator.core

from simulator.mapping import mapping


def switch_mode(intro, mode, exit_action=None):
        return ('切换到 {0} 模式'.format(intro),
                lambda _: mapping.mode_switch(mode, exit_action))


def click(x, y, key='left', hwnd=None, wait=.1):
        if hwnd is None:
                simulator.core.mouse.click(key, x, y, hwnd, wait)
        else:
                simulator.core.mouseBack.click(key, x, y, hwnd, wait)


def input_key(key, hwnd):
        if hwnd is None:
                simulator.core.keyboard.input_key(key)
        else:
                simulator.core.keyboardBack.input_key(key, hwnd)
