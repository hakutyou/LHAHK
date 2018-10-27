# coding=utf-8

__all__ = ['mouseMapping']

from simulator.mouseInfo import mouseInfo
import simulator.core
import interactive

from . import general_lib
from . import base
from . import normal


class MouseMapping(base.BaseMapping):
        """
        mouse: 鼠标模式
        """

        def __init__(self):
                super(__class__, self).__init__()
                self.MODE = 'mouse'
                self._speed = 0

        @property
        def speed(self):
                if self._speed < 1:
                        return 1
                return self._speed

        def press(self):
                result = {
                        '0000*0': self.speed_set(0),
                        '0000*1': self.speed_set(1),
                        '0000*2': self.speed_set(2),
                        '0000*3': self.speed_set(3),
                        '0000*4': self.speed_set(4),
                        '0000*5': self.speed_set(5),
                        '0000*6': self.speed_set(6),
                        '0000*7': self.speed_set(7),
                        '0000*8': self.speed_set(8),
                        '0000*9': self.speed_set(9),
                        '0000*Q': self.speed_set(None),
                        '0000*E': self.speed_get(),
                        '0000*F': self.mouse_click('left', 1),
                        '0000*G': self.mouse_click('right', 1),
                        '0000*R': self.mouse_position(),
                        '0000*W': self.move('W'),
                        '0000*S': self.move('S'),
                        '0000*A': self.move('A'),
                        '0000*D': self.move('D'),
                        '0000*Up': self.move('W'),
                        '0000*Down': self.move('S'),
                        '0000*Left': self.move('A'),
                        '0000*Right': self.move('D')
                }
                result.update({'*Escape': general_lib.switch_mode(normal.normalMapping)})
                result.update(super(__class__, self).press())
                return result

        def release(self):
                result = {
                        '0000*F': self.mouse_click('left', 0),
                        '0000*G': self.mouse_click('right', 0),
                }
                result.update(super(__class__, self).press())
                return result

        def speed_set(self, number):
                def __speed_set(_):
                        if number is None:
                                self._speed = 0
                                return
                        self._speed *= 10
                        if self._speed > 10000:
                                self._speed = 0
                        self._speed += number

                return '修改速度', __speed_set

        def speed_get(self):
                def __speed_get(_):
                        interactive.qmlCaller.tray_info('Speed', str(self._speed))

                return '查看速度', __speed_get

        def move(self, direct):
                def __move(_):
                        x, y = mouseInfo.mouse_position()
                        if direct == 'W':
                                y -= self.speed
                        elif direct == 'S':
                                y += self.speed
                        elif direct == 'A':
                                x -= self.speed
                        else:
                                x += self.speed
                        simulator.core.mouse.move(x, y)

                return '移动', __move

        @staticmethod
        def mouse_click(button, state):
                def __mouse_click(_):
                        simulator.core.mouse.key_once(button, state)

                return '点击', __mouse_click

        @staticmethod
        def mouse_position():
                def __mouse_position(_):
                        x, y = mouseInfo.mouse_position()
                        interactive.qmlCaller.tray_info('Mouse', 'x:{0}, y:{1}'.format(x, y))

                return '鼠标位置', __mouse_position


mouseMapping = MouseMapping()
