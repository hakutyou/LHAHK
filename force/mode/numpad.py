# coding=utf-8

__all__ = ['MODE', 'press', 'release']

import force.core
from external.readfile import Readfile

from . import general_lib
from . import normal

MODE = 'numpad'


def press() -> dict:
        mapper = Readfile('force/mode/numpad_press.txt')
        result = dict(map(lambda x: (x, _key_remap(mapper.value[x])), mapper.value))
        result.update({'*Escape': general_lib.switch_mode(normal)})
        return result


def release() -> dict:
        mapper = Readfile('force/mode/numpad_release.txt')
        result = dict(map(lambda x: (x, _key_remap(mapper.value[x])), mapper.value))
        return result


def _key_remap(arg):
        output = arg[0]
        state = arg[1]
        if state:
                def procedure(_):
                        return force.core.keyboard.press(output)
        else:
                def procedure(_):
                        return force.core.keyboard.release(output)
        return output, procedure
