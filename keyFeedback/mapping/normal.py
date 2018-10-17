__all__ = ['normalMapping']

from ..base import key
from ..base import mapping

from . import base
from . import numpad
from . import advance


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
                        "#['A']": self._print_window_title,
                        "#['S']": lambda _: mapping.mode_switch(advance.advanceMapping),
                        "#['D']": lambda _: key.hold('left_win'),
                        "#['Rshift', 'A']": lambda _: mapping.mode_switch(
                                numpad.numpadMapping),
                }, **super().press())

        def release(self):
                return {
                        "['D']": lambda _: key.release('left_win'),
                }

        def _print_window_title(self, window_name: str):
                """
                打印激活窗口标题
                """
                if self._action_head(self._print_window_title):
                        return
                print(window_name)


normalMapping = _NormalMapping()
