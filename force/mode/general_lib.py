# coding=utf-8

__all__ = ['switch_mode']

from force.mapping import mapping


def switch_mode(mode, exit_action=None):
        return ('切换到 {0} 模式'.format(mode.MODE),
                lambda _: mapping.mode_switch(mode, exit_action))
