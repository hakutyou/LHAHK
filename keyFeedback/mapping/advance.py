__all__ = ['advanceMapping']

from ..base import key
from ..base import mapping

from . import base
from . import normal


class _AdvanceMapping(base.BaseMapping):
        def __init__(self):
                super().__init__()
                self.MODE = 'advance'

        def press(self):
                return dict({
                        "#['A']": self.reverse_window_title,
                        "#['S']": lambda _: mapping.mode_switch(normal.normalMapping),
                        "#['D']": lambda _: key.hold('left_win'),
                }, **super().press())

        def release(self):
                return {
                        "['D']": lambda _: key.release('left_win'),
                }

        @staticmethod
        def reverse_window_title(window_name: str):
                print(window_name[::-1])


advanceMapping = _AdvanceMapping()
