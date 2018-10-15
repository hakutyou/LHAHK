__all__ = ['normalMapping']

from ..base import key
from ..base import mapping

from . import base
from . import numpad
from . import advance


class _NormalMapping(base.BaseMapping):
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

        @staticmethod
        def _print_window_title(window_name: str):
                print(window_name)


normalMapping = _NormalMapping()
