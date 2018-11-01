# coding=utf-8

__all__ = ['numpadMapping']

import force.core
from external.readfile import Readfile

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

        @property
        def press(self) -> dict:
                mapper = Readfile('force/mode/numpad_press.txt')
                result = dict(map(lambda x: (x, self.__key_remap(mapper.value[x])), mapper.value))
                result.update({'*Escape': general_lib.switch_mode(normal.normalMapping)})
                result.update(super(__class__, self).press)
                return result

        @property
        def release(self) -> dict:
                mapper = Readfile('force/mode/numpad_release.txt')
                result = dict(map(lambda x: (x, self.__key_remap(mapper.value[x])), mapper.value))
                result.update(super(__class__, self).release)
                return result

        @staticmethod
        def __key_remap(arg):
                output = arg[0]
                state = arg[1]
                if state:
                        def procedure(_):
                                return force.core.keyboard.press(output)
                else:
                        def procedure(_):
                                return force.core.keyboard.release(output)
                return output, procedure


numpadMapping = _NumpadMapping()
