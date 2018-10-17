__all__ = ['advanceMapping']

from ..base import key
from ..base import mapping

from . import base
from . import normal


class _AdvanceMapping(base.BaseMapping):
        """
        Advance: 命令模式
        可切换以下模式 [S]: Normal
        """
        def __init__(self):
                super().__init__()
                self.MODE = 'advance'

        def press(self):
                return dict({
                        "#['A']": self._reverse_window_title,
                        "#['S']": lambda _: mapping.mode_switch(normal.normalMapping),
                        "#['D']": lambda _: key.hold('left_win'),
                }, **super().press())

        def release(self):
                return {
                        "['D']": lambda _: key.release('left_win'),
                }

        def _reverse_window_title(self, window_name: str):
                """
                反向打印激活窗口标题
                """
                if self._action_head(self._reverse_window_title):
                        return
                print(window_name[::-1])


advanceMapping = _AdvanceMapping()
