# coding=utf-8

__all__ = ['numpadMapping']

import simulator.core

from . import general_lib
from . import base
from . import normal


class _NumpadMapping(base.BaseMapping):
        """
        numpad: 小键盘模式
        """

        def __init__(self):
                super(__class__, self).__init__()
                self.MODE = 'numpad'

        def press(self):
                mapper = {
                        '0000*Q': ('Numpad7', True),
                        '0000*W': ('Numpad8', True),
                        '0000*E': ('Numpad9', True),
                        '0000*A': ('Numpad4', True),
                        '0000*S': ('Numpad5', True),
                        '0000*D': ('Numpad6', True),
                        '0000*Z': ('Numpad1', True),
                        '0000*X': ('Numpad2', True),
                        '0000*C': ('Numpad3', True),
                        '0000*V': ('Numpad0', True),

                        '0000*7': ('Numpad7', True),
                        '0000*8': ('Numpad8', True),
                        '0000*9': ('Numpad9', True),
                        '0000*4': ('Numpad4', True),
                        '0000*5': ('Numpad5', True),
                        '0000*6': ('Numpad6', True),
                        '0000*1': ('Numpad1', True),
                        '0000*2': ('Numpad2', True),
                        '0000*3': ('Numpad3', True),

                        '0002*Oem_Plus': ('Add', True),  # +
                        '0000*Oem_Minus': ('Subtract', True),  # -
                        '0000*Oem_2': ('Divide', True),  # /
                        '0002*8': ('Multiply', True),  # *
                }
                result = dict(map(lambda x: (x, self._key_remap(mapper[x])), mapper))

                result.update({'*Escape': general_lib.switch_mode(normal.normalMapping)})
                result.update(super(__class__, self).press())
                return result

        def release(self):
                mapper = {
                        '0000*Q': ('Numpad7', False),
                        '0000*W': ('Numpad8', False),
                        '0000*E': ('Numpad9', False),
                        '0000*A': ('Numpad4', False),
                        '0000*S': ('Numpad5', False),
                        '0000*D': ('Numpad6', False),
                        '0000*Z': ('Numpad1', False),
                        '0000*X': ('Numpad2', False),
                        '0000*C': ('Numpad3', False),
                        '0000*V': ('Numpad0', False),

                        '0000*7': ('Numpad7', False),
                        '0000*8': ('Numpad8', False),
                        '0000*9': ('Numpad9', False),
                        '0000*4': ('Numpad4', False),
                        '0000*5': ('Numpad5', False),
                        '0000*6': ('Numpad6', False),
                        '0000*1': ('Numpad1', False),
                        '0000*2': ('Numpad2', False),
                        '0000*3': ('Numpad3', False),

                        '0002*Oem_Plus': ('Add', False),  # +
                        '0000*Oem_Minus': ('Subtract', False),  # -
                        '0000*Oem_2': ('Divide', False),  # /
                        '0002*8': ('Multiply', False),  # *
                }
                result = dict(map(lambda x: (x, self._key_remap(mapper[x])), mapper))
                result.update(super(__class__, self).release())
                return result

        @staticmethod
        def _key_remap(arg):
                output = arg[0]
                state = arg[1]
                if state:
                        def procedure(_):
                                return simulator.core.keyboard.press(output)
                else:
                        def procedure(_):
                                return simulator.core.keyboard.release(output)
                        # procedure = lambda _: simulator.core.keyboard.release(output)
                return output, procedure


numpadMapping = _NumpadMapping()
