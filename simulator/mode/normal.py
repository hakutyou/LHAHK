__all__ = ['normalMapping']

from . import general_lib

from . import base
from . import numpad
from . import wuxia


class _NormalMapping(base.BaseMapping):
        """
        normal: 普通模式
        """
        def __init__(self):
                super().__init__()
                self.MODE = 'normal'

        def press(self):
                return dict({
                        "2#['A']": general_lib.switch_mode('numpad', numpad.numpadMapping),
                        "2#['F10']": general_lib.switch_mode('wuxia', wuxia.wuxiaMapping),
                }, **super().press())

        def release(self):
                return dict({
                }, **super().release())

        # @staticmethod
        # def _print_window_title(window_name: str):
        #         """
        #         打印激活窗口标题
        #         """
        #         print(window_name)


normalMapping = _NormalMapping()
