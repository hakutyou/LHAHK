__all__ = ['numpadMapping']

from ..base import mapping
from .. import simulation

from . import base
from . import normal


class _NumpadMapping(base.BaseMapping):
        """
        Numpad: 小键盘模式
        可切换以下模式 [Rshift, A]: Normal
        """
        def __init__(self):
                super().__init__()
                self.MODE = 'numpad'

        def press(self):
                return dict({
                        '*Q': lambda _: simulation.press('numpad_7'),
                        '*W': lambda _: simulation.press('numpad_8'),
                        '*E': lambda _: simulation.press('numpad_9'),
                        '*A': lambda _: simulation.press('numpad_4'),
                        '*S': lambda _: simulation.press('numpad_5'),
                        '*D': lambda _: simulation.press('numpad_6'),
                        '*Z': lambda _: simulation.press('numpad_1'),
                        '*X': lambda _: simulation.press('numpad_2'),
                        '*C': lambda _: simulation.press('numpad_3'),

                        '*7': lambda _: simulation.press('numpad_7'),
                        '*8': lambda _: simulation.press('numpad_8'),
                        '*9': lambda _: simulation.press('numpad_9'),
                        '*4': lambda _: simulation.press('numpad_4'),
                        '*5': lambda _: simulation.press('numpad_5'),
                        '*6': lambda _: simulation.press('numpad_6'),
                        '*1': lambda _: simulation.press('numpad_1'),
                        '*2': lambda _: simulation.press('numpad_2'),
                        '*3': lambda _: simulation.press('numpad_3'),

                        "#['Rshift', 'A']": lambda _: mapping.mode_switch(
                                normal.normalMapping),
                }, **super().press())

        def release(self):
                return {
                        '*Q': lambda _: simulation.release('numpad_7'),
                        '*W': lambda _: simulation.release('numpad_8'),
                        '*E': lambda _: simulation.release('numpad_9'),
                        '*A': lambda _: simulation.release('numpad_4'),
                        '*S': lambda _: simulation.release('numpad_5'),
                        '*D': lambda _: simulation.release('numpad_6'),
                        '*Z': lambda _: simulation.release('numpad_1'),
                        '*X': lambda _: simulation.release('numpad_2'),
                        '*C': lambda _: simulation.release('numpad_3'),

                        "*7": lambda _: simulation.release('numpad_7'),
                        "*8": lambda _: simulation.release('numpad_8'),
                        "*9": lambda _: simulation.release('numpad_9'),
                        "*4": lambda _: simulation.release('numpad_4'),
                        "*5": lambda _: simulation.release('numpad_5'),
                        "*6": lambda _: simulation.release('numpad_6'),
                        "*1": lambda _: simulation.release('numpad_1'),
                        "*2": lambda _: simulation.release('numpad_2'),
                        "*3": lambda _: simulation.release('numpad_3'),
                }


numpadMapping = _NumpadMapping()
