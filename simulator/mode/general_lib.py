__all__ = ['switch_normal']

from ..mapping import mapping

from . import normal


def switch_normal(_):
        """
        切换到 normal 模式
        """
        mapping.mode_switch(normal.normalMapping)
