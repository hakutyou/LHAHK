__all__ = ['numpadMapping']

from .. import simulation

from . import general_lib
from . import base


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
                        "['Q']": lambda _: simulation.press('Numpad7'),
                        "['W']": lambda _: simulation.press('Numpad8'),
                        "['E']": lambda _: simulation.press('Numpad9'),
                        "['A']": lambda _: simulation.press('Numpad4'),
                        "['S']": lambda _: simulation.press('Numpad5'),
                        "['D']": lambda _: simulation.press('Numpad6'),
                        "['Z']": lambda _: simulation.press('Numpad1'),
                        "['X']": lambda _: simulation.press('Numpad2'),
                        "['C']": lambda _: simulation.press('Numpad3'),

                        '*7': lambda _: simulation.press('Numpad7'),
                        '*8': lambda _: simulation.press('Numpad8'),
                        '*9': lambda _: simulation.press('Numpad9'),
                        '*4': lambda _: simulation.press('Numpad4'),
                        '*5': lambda _: simulation.press('Numpad5'),
                        '*6': lambda _: simulation.press('Numpad6'),
                        '*1': lambda _: simulation.press('Numpad1'),
                        '*2': lambda _: simulation.press('Numpad2'),
                        '*3': lambda _: simulation.press('Numpad3'),
                        '*0': lambda _: simulation.press('Numpad0'),
                        "['Rshift', 'Oem_Plus']": lambda _: simulation.press('Add'),  # +
                        "['Oem_Minus']": lambda _: simulation.press('Subtract'),      # -
                        "['Oem_2']": lambda _: simulation.press('Divide'),            # /
                        "['Rshift', '8']": lambda _: simulation.press('Multiply'),    # *

                        '*Escape': general_lib.switch_normal,
                }, **super().press())

        def release(self):
                return dict({
                        "['Q']": lambda _: simulation.release('Numpad7'),
                        "['W']": lambda _: simulation.release('Numpad8'),
                        "['E']": lambda _: simulation.release('Numpad9'),
                        "['A']": lambda _: simulation.release('Numpad4'),
                        "['S']": lambda _: simulation.release('Numpad5'),
                        "['D']": lambda _: simulation.release('Numpad6'),
                        "['Z']": lambda _: simulation.release('Numpad1'),
                        "['X']": lambda _: simulation.release('Numpad2'),
                        "['C']": lambda _: simulation.release('Numpad3'),

                        '*7': lambda _: simulation.release('Numpad7'),
                        '*8': lambda _: simulation.release('Numpad8'),
                        '*9': lambda _: simulation.release('Numpad9'),
                        '*4': lambda _: simulation.release('Numpad4'),
                        '*5': lambda _: simulation.release('Numpad5'),
                        '*6': lambda _: simulation.release('Numpad6'),
                        '*1': lambda _: simulation.release('Numpad1'),
                        '*2': lambda _: simulation.release('Numpad2'),
                        '*3': lambda _: simulation.release('Numpad3'),
                        "['Rshift', 'Oem_Plus']": lambda _: simulation.release('Add'),  # +
                        "['Oem_Minus']": lambda _: simulation.release('Subtract'),      # -
                        "['Oem_2']": lambda _: simulation.release('Divide'),            # /
                        "['Rshift', '8']": lambda _: simulation.release('Multiply'),    # *
                }, **super().release())


numpadMapping = _NumpadMapping()
