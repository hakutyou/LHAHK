__all__ = ['numpadMapping']

from .. import core

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
                        "['Q']": lambda _: core.keyboardGlob.press('Numpad7'),
                        "['W']": lambda _: core.keyboardGlob.press('Numpad8'),
                        "['E']": lambda _: core.keyboardGlob.press('Numpad9'),
                        "['A']": lambda _: core.keyboardGlob.press('Numpad4'),
                        "['S']": lambda _: core.keyboardGlob.press('Numpad5'),
                        "['D']": lambda _: core.keyboardGlob.press('Numpad6'),
                        "['Z']": lambda _: core.keyboardGlob.press('Numpad1'),
                        "['X']": lambda _: core.keyboardGlob.press('Numpad2'),
                        "['C']": lambda _: core.keyboardGlob.press('Numpad3'),

                        '*7': lambda _: core.keyboardGlob.press('Numpad7'),
                        '*8': lambda _: core.keyboardGlob.press('Numpad8'),
                        '*9': lambda _: core.keyboardGlob.press('Numpad9'),
                        '*4': lambda _: core.keyboardGlob.press('Numpad4'),
                        '*5': lambda _: core.keyboardGlob.press('Numpad5'),
                        '*6': lambda _: core.keyboardGlob.press('Numpad6'),
                        '*1': lambda _: core.keyboardGlob.press('Numpad1'),
                        '*2': lambda _: core.keyboardGlob.press('Numpad2'),
                        '*3': lambda _: core.keyboardGlob.press('Numpad3'),
                        '*0': lambda _: core.keyboardGlob.press('Numpad0'),
                        "['Rshift', 'Oem_Plus']": lambda _: core.keyboardGlob.press('Add'),  # +
                        "['Oem_Minus']": lambda _: core.keyboardGlob.press('Subtract'),      # -
                        "['Oem_2']": lambda _: core.keyboardGlob.press('Divide'),            # /
                        "['Rshift', '8']": lambda _: core.keyboardGlob.press('Multiply'),    # *

                        '*Escape': general_lib.switch_normal,
                }, **super().press())

        def release(self):
                return dict({
                        "['Q']": lambda _: core.keyboardGlob.release('Numpad7'),
                        "['W']": lambda _: core.keyboardGlob.release('Numpad8'),
                        "['E']": lambda _: core.keyboardGlob.release('Numpad9'),
                        "['A']": lambda _: core.keyboardGlob.release('Numpad4'),
                        "['S']": lambda _: core.keyboardGlob.release('Numpad5'),
                        "['D']": lambda _: core.keyboardGlob.release('Numpad6'),
                        "['Z']": lambda _: core.keyboardGlob.release('Numpad1'),
                        "['X']": lambda _: core.keyboardGlob.release('Numpad2'),
                        "['C']": lambda _: core.keyboardGlob.release('Numpad3'),

                        '*7': lambda _: core.keyboardGlob.release('Numpad7'),
                        '*8': lambda _: core.keyboardGlob.release('Numpad8'),
                        '*9': lambda _: core.keyboardGlob.release('Numpad9'),
                        '*4': lambda _: core.keyboardGlob.release('Numpad4'),
                        '*5': lambda _: core.keyboardGlob.release('Numpad5'),
                        '*6': lambda _: core.keyboardGlob.release('Numpad6'),
                        '*1': lambda _: core.keyboardGlob.release('Numpad1'),
                        '*2': lambda _: core.keyboardGlob.release('Numpad2'),
                        '*3': lambda _: core.keyboardGlob.release('Numpad3'),
                        "['Rshift', 'Oem_Plus']": lambda _: core.keyboardGlob.release('Add'),  # +
                        "['Oem_Minus']": lambda _: core.keyboardGlob.release('Subtract'),      # -
                        "['Oem_2']": lambda _: core.keyboardGlob.release('Divide'),            # /
                        "['Rshift', '8']": lambda _: core.keyboardGlob.release('Multiply'),    # *
                }, **super().release())


numpadMapping = _NumpadMapping()
