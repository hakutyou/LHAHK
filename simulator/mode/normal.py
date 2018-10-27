# coding=utf-8

__all__ = ['normalMapping']

from . import general_lib
from . import base
from . import numpad
from . import wuxia
from . import mouse


class _NormalMapping(base.BaseMapping):
        """
        normal: 普通模式
        """
        def __init__(self):
                super(__class__, self).__init__()
                self.MODE = 'normal'

        def press(self):
                result = {
                        "0002#['A']": general_lib.switch_mode(numpad.numpadMapping),
                        "0002#['Q']": general_lib.switch_mode(mouse.mouseMapping),
                        "0002#['F10']": general_lib.switch_mode(wuxia.wuxiaMapping),
                }
                result.update(super(__class__, self).press())
                return result

        def release(self):
                result = {}
                result.update(super(__class__, self).press())
                return result

        # @staticmethod
        # def _print_window_title(window_name: str):
        #         """
        #         打印激活窗口标题
        #         """
        #         print(window_name)


normalMapping = _NormalMapping()
