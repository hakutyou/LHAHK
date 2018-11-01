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

        @property
        def press(self) -> dict:
                result = {
                        "0002#['A']": general_lib.switch_mode(numpad.numpadMapping),
                        "0002#['Z']": general_lib.switch_mode(mouse.mouseMapping),
                        "0002#['X']": general_lib.switch_mode(wuxia.wuxiaMapping),
                }
                result.update(super(__class__, self).press)
                return result

        @property
        def release(self) -> dict:
                result = {}
                result.update(super(__class__, self).release)
                return result

        # @staticmethod
        # def _print_window_title(window_name: str):
        #         """
        #         打印激活窗口标题
        #         """
        #         print(window_name)


normalMapping = _NormalMapping()
