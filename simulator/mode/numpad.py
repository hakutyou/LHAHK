__all__ = ['numpadMapping']

from .. import core

from . import normal
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
                mapper = {
                        "['Q']": ('Numpad7', True),
                        "['W']": ('Numpad8', True),
                        "['E']": ('Numpad9', True),
                        "['A']": ('Numpad4', True),
                        "['S']": ('Numpad5', True),
                        "['D']": ('Numpad6', True),
                        "['Z']": ('Numpad1', True),
                        "['X']": ('Numpad2', True),
                        "['C']": ('Numpad3', True),

                        '*7': ('Numpad7', True),
                        '*8': ('Numpad8', True),
                        '*9': ('Numpad9', True),
                        '*4': ('Numpad4', True),
                        '*5': ('Numpad5', True),
                        '*6': ('Numpad6', True),
                        '*1': ('Numpad1', True),
                        '*2': ('Numpad2', True),
                        '*3': ('Numpad3', True),

                        "['Rshift', 'Oem_Plus']": ('Add', True),  # +
                        "['Oem_Minus']": ('Subtract', True),  # -
                        "['Oem_2']": ('Divide', True),  # /
                        "['Rshift', '8']": ('Multiply', True),  # *
                }
                result = dict(map(lambda x: (x, self._key_remap(mapper[x])), mapper))

                result.update({'*Escape': general_lib.switch_mode('normal', normal.normalMapping)})
                result.update(super().press())
                return result

        def release(self):
                mapper = {
                        "['Q']": ('Numpad7', False),
                        "['W']": ('Numpad8', False),
                        "['E']": ('Numpad9', False),
                        "['A']": ('Numpad4', False),
                        "['S']": ('Numpad5', False),
                        "['D']": ('Numpad6', False),
                        "['Z']": ('Numpad1', False),
                        "['X']": ('Numpad2', False),
                        "['C']": ('Numpad3', False),

                        '*7': ('Numpad7', False),
                        '*8': ('Numpad8', False),
                        '*9': ('Numpad9', False),
                        '*4': ('Numpad4', False),
                        '*5': ('Numpad5', False),
                        '*6': ('Numpad6', False),
                        '*1': ('Numpad1', False),
                        '*2': ('Numpad2', False),
                        '*3': ('Numpad3', False),

                        "['Rshift', 'Oem_Plus']": ('Add', False),  # +
                        "['Oem_Minus']": ('Subtract', False),  # -
                        "['Oem_2']": ('Divide', False),  # /
                        "['Rshift', '8']": ('Multiply', False),  # *
                }
                result = dict(map(lambda x: (x, self._key_remap(mapper[x])), mapper))
                result.update(super().release())
                return result

        @staticmethod
        def _key_remap(arg):
                output = arg[0]
                state = arg[1]
                if state:
                        procedure = lambda _: core.keyboard.press(output)
                else:
                        procedure = lambda _: core.keyboard.release(output)
                return output, procedure


numpadMapping = _NumpadMapping()
