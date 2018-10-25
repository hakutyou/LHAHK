__all__ = ['normalMapping']

from ..mapping import mapping

from . import base
from . import numpad
from . import wuxia


class _NormalMapping(base.BaseMapping):
        """
        Normal: 普通模式
        可切换以下模式 [Rshift, A]: Numpad, [S]: Advance
        """
        def __init__(self):
                super().__init__()
                self.MODE = 'normal'

        def press(self):
                return dict({
                        "#['Rshift', 'A']": self._switch_numpad,
                        "#['Rshift', 'F10']": self._switch_wuxia,
                }, **super().press())

        def release(self):
                return dict({
                }, **super().release())

        @staticmethod
        def _print_window_title(window_name: str):
                """
                打印激活窗口标题
                """
                print(window_name)

        @staticmethod
        def _switch_numpad(_):
                """
                切换到 numpad 模式
                """
                mapping.mode_switch(numpad.numpadMapping)

        @staticmethod
        def _switch_wuxia(_):
                """
                切换到 wuxia 模式
                """
                mapping.mode_switch(wuxia.wuxiaMapping)


normalMapping = _NormalMapping()
