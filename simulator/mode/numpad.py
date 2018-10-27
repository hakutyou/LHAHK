__all__ = ['numpadMapping']

from .. import core

from . import normal
from . import general_lib
from . import base


class _NumpadMapping(base.BaseMapping):
        """
        numpad: 小键盘模式
        """

        def __init__(self):
                super().__init__()
                self.MODE = 'numpad'

        def press(self):
                mapper = {
                        '0*Q': ('Numpad7', True),
                        '0*W': ('Numpad8', True),
                        '0*E': ('Numpad9', True),
                        '0*A': ('Numpad4', True),
                        '0*S': ('Numpad5', True),
                        '0*D': ('Numpad6', True),
                        '0*Z': ('Numpad1', True),
                        '0*X': ('Numpad2', True),
                        '0*C': ('Numpad3', True),

                        '0*7': ('Numpad7', True),
                        '0*8': ('Numpad8', True),
                        '0*9': ('Numpad9', True),
                        '0*4': ('Numpad4', True),
                        '0*5': ('Numpad5', True),
                        '0*6': ('Numpad6', True),
                        '0*1': ('Numpad1', True),
                        '0*2': ('Numpad2', True),
                        '0*3': ('Numpad3', True),

                        '2*Oem_Plus': ('Add', True),  # +
                        '0*Oem_Minus': ('Subtract', True),  # -
                        '0*Oem_2': ('Divide', True),  # /
                        '2*8': ('Multiply', True),  # *
                }
                result = dict(map(lambda x: (x, self._key_remap(mapper[x])), mapper))

                result.update({'*Escape': general_lib.switch_mode('normal', normal.normalMapping)})
                result.update(super().press())
                return result

        def release(self):
                mapper = {
                        '0*Q': ('Numpad7', False),
                        '0*W': ('Numpad8', False),
                        '0*E': ('Numpad9', False),
                        '0*A': ('Numpad4', False),
                        '0*S': ('Numpad5', False),
                        '0*D': ('Numpad6', False),
                        '0*Z': ('Numpad1', False),
                        '0*X': ('Numpad2', False),
                        '0*C': ('Numpad3', False),

                        '0*7': ('Numpad7', False),
                        '0*8': ('Numpad8', False),
                        '0*9': ('Numpad9', False),
                        '0*4': ('Numpad4', False),
                        '0*5': ('Numpad5', False),
                        '0*6': ('Numpad6', False),
                        '0*1': ('Numpad1', False),
                        '0*2': ('Numpad2', False),
                        '0*3': ('Numpad3', False),

                        '2*Oem_Plus': ('Add', False),  # +
                        '0*Oem_Minus': ('Subtract', False),  # -
                        '0*Oem_2': ('Divide', False),  # /
                        '2*8': ('Multiply', False),  # *
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
