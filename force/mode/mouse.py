# coding=utf-8

__all__ = ['MODE', 'press', 'release']

import force
import force.core
import dmail
import visual
# import network

from . import general_lib
from . import normal

MODE = 'mouse'
__speed = 0
__key = 0x0
__key_mapper = {
        'left': 0b0001,
        'right': 0b0010,
        'crop': 0b00010000,
}
# resnet = network.resnet.create()


def press() -> dict:
        result = {
                '0000*0': _speed_set(0),
                '0000*1': _speed_set(1),
                '0000*2': _speed_set(2),
                '0000*3': _speed_set(3),
                '0000*4': _speed_set(4),
                '0000*5': _speed_set(5),
                '0000*6': _speed_set(6),
                '0000*7': _speed_set(7),
                '0000*8': _speed_set(8),
                '0000*9': _speed_set(9),
                '0000*X': _speed_set(None),
                '0000*Z': _speed_get(),
                '0000#Q': _mouse_click('left', 1),
                '0000#E': _mouse_click('right', 1),
                '0000*R': _mouse_position(),
                '0000*W': _move('W'),
                '0000*S': _move('S'),
                '0000*A': _move('A'),
                '0000*D': _move('D'),
                '0000*Up': _move('W'),
                '0000*Down': _move('S'),
                '0000*Left': _move('A'),
                '0000*Right': _move('D'),
                '0000#P': _crop(True),
                '0000#O': _show(),
                # '0000#I': _mnist(),
        }
        result.update({'*Escape': general_lib.switch_mode(normal, exit_action)})
        return result


def release() -> dict:
        return {
                '*Q': _mouse_click('left', 0),
                '*E': _mouse_click('right', 0),
                '*P': _crop(False),
        }


def exit_action(_) -> None:
        for button in ['left', 'right']:
                if __key & __key_mapper[button]:
                        force.core.mouse.real_mouse_up(button)


def _speed_set(number):
        def __speed_set(_):
                global __speed
                if number is None:
                        __speed = 0
                        return
                __speed *= 10
                if __speed > 10000:
                        __speed = 0
                __speed += number

        return '修改速度', __speed_set


def _speed_get():
        def __speed_get(_):
                dmail.qmlCaller.tray_info('Speed', str(__speed))

        return '查看速度', __speed_get


def _move(direct):
        def __move_speed():
                if __speed < 1:
                        return 1
                return __speed

        def __move(_):
                x, y = force.mouseInfo.mouse_position()
                if direct == 'W':
                        y -= __move_speed()
                elif direct == 'S':
                        y += __move_speed()
                elif direct == 'A':
                        x -= __move_speed()
                else:
                        x += __move_speed()
                force.core.mouse.real_move(x, y)

        return '移动', __move


def _mouse_click(button, state):
        def __mouse_click(_):
                global __key
                if state == 1:
                        __key |= __key_mapper[button]
                else:
                        if not __key & __key_mapper[button]:
                                return
                        __key &= ~__key_mapper[button]
                force.core.mouse.real_key_once(button, state)

        return '点击', __mouse_click


def _mouse_position():
        def __mouse_position(hwnd):
                x, y = force.mouseInfo.mouse_position()
                x_win, y_win, _, _ = force.mouseInfo.window_position(hwnd)
                dmail.qmlCaller.tray_info('Mouse', 'x:{0}, y:{1}\nx:{2}, y:{3}'.format(
                        x, y, x - x_win, y - y_win))

        return '鼠标位置', __mouse_position


__crop_start_x = 0
__crop_start_y = 0
__crop_end_x = 0
__crop_end_y = 0


def _crop(start: bool):
        def __check_and_crop(hwnd):
                global __key, __crop_start_x, __crop_end_x, __crop_start_y, __crop_end_y
                if start:
                        __key |= __key_mapper['crop']
                        __crop_start_x, __crop_start_y = force.mouseInfo.mouse_position(hwnd)
                else:
                        if not __key & __key_mapper['crop']:
                                return
                        __key &= ~__key_mapper['crop']
                        __crop_end_x, __crop_end_y = force.mouseInfo.mouse_position(hwnd)

        return '选定截图', __check_and_crop


def _show():
        def __show(hwnd):
                image = visual.Image()
                image.shot(hwnd)
                image.crop(min(__crop_start_x, __crop_end_x), min(__crop_start_y, __crop_end_y),
                           abs(__crop_start_x - __crop_end_x), abs(__crop_start_y - __crop_end_y))
                image.show()

        return '截图', __show


# def _mnist():
#         def __mnist(hwnd):
#                 image = visual.Image()
#                 image.shot(hwnd)
#                 image.crop(min(__crop_start_x, __crop_end_x), min(__crop_start_y, __crop_end_y),
#                            abs(__crop_start_x - __crop_end_x), abs(__crop_start_y - __crop_end_y))
#                 image.resize(28, 28)
#                 image.grey()
#                 arr = visual.imath.binary(visual.imath.transform_array(image))
#                 network.resnet.build(resnet)
#                 print(network.resnet.read(resnet, arr.flatten()))
#
#         return 'MNIST', __mnist

# resnet = network.ResNet()
# resnet.build()
# image = visual.Image()
# image.open('C:/Users/kakoi/Desktop/1.png')
# image.grey()
# arr = visual.imath.binary(visual.imath.transform_array(image)).flatten() / 255
# print(arr)
# # image.read(arr)
# # image.show()
# print(resnet.read(arr))
