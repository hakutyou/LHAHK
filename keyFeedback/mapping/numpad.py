__all__ = ['numpadMapping']

from ..base import key
from ..base import mapping

from . import base
from . import normal


class _NumpadMapping(base.BaseMapping):
        def __init__(self):
                super().__init__()
                self.MODE = 'numpad'

        def press(self):
                return dict({
                        "*Q": lambda _: key.hold('numpad_7'),
                        "*W": lambda _: key.hold('numpad_8'),
                        "*E": lambda _: key.hold('numpad_9'),
                        "*A": lambda _: key.hold('numpad_4'),
                        "*S": lambda _: key.hold('numpad_5'),
                        "*D": lambda _: key.hold('numpad_6'),
                        "*Z": lambda _: key.hold('numpad_1'),
                        "*X": lambda _: key.hold('numpad_2'),
                        "*C": lambda _: key.hold('numpad_3'),
                        "#['Rshift', 'A']": lambda _: mapping.mode_switch(
                                normal.normalMapping),
                }, **super().press())

        def release(self):
                return {
                        "*Q": lambda _: key.release('numpad_7'),
                        "*W": lambda _: key.release('numpad_8'),
                        "*E": lambda _: key.release('numpad_9'),
                        "*A": lambda _: key.release('numpad_4'),
                        "*S": lambda _: key.release('numpad_5'),
                        "*D": lambda _: key.release('numpad_6'),
                        "*Z": lambda _: key.release('numpad_1'),
                        "*X": lambda _: key.release('numpad_2'),
                        "*C": lambda _: key.release('numpad_3'),
                }


numpadMapping = _NumpadMapping()