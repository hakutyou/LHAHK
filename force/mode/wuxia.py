# coding=utf-8

__all__ = ['MODE', 'press', 'release']

import threading
import general
import force.core
import force.mouseInfo

from . import general_lib
from . import normal

MODE = 'wuxia'
__hwnd = None
__mouse_x, __mouse_y = 0, 0
__rush_flags = False


def press() -> dict:
        result = {
                '0002*F2': _choose_hwnd(),
                '0002*F3': _cancel_hwnd(),
                '0002*F5': _clear_auction(1),
                '0002*F6': _rush_voyage(4),
                '0002*F7': _rush_voyage(5),
                '0002*F8': _rush_key(['W', 'G'], 1),
                '0002*F9': _rush_click(),
                '0002*F10': _rush_stop(),
                '0002*F11': _rush_key(['F'], 0),
        }
        result.update({'*Escape': general_lib.switch_mode(normal, _rush_stop()[1])})
        return result


def release() -> dict:
        return {}


def _choose_hwnd():
        def __choose_hwnd(hwnd):
                global __hwnd, __mouse_x, __mouse_y
                __hwnd = hwnd
                __mouse_x, __mouse_y = force.mouseInfo.mouse_position(hwnd)

        return '锁定激活窗口', __choose_hwnd


def _cancel_hwnd():
        def __cancel_hwnd(_):
                global __hwnd
                __hwnd = None

        return '取消窗口锁定', __cancel_hwnd


def _rush_stop():
        def __rush_stop(_):
                global __rush_flags
                __rush_flags = False

        return '取消连续', __rush_stop


def _rush_voyage(hosi):
        def __rush_voyage_thread():
                while __rush_flags:
                        force.core.mouse.click('left', 820, 180, __hwnd, wait_time=.2)
                        general.random_wait()
                        if hosi == 4:
                                force.core.mouse.click('right', 662 - 1, 351 - 26, __hwnd)
                        if hosi == 5:
                                force.core.mouse.click('right', 471 - 1, 423 - 26, __hwnd)
                        general.random_wait()
                        force.core.mouse.click('left', 971, 535, __hwnd)
                        general.random_wait()

        def __rush_voyage(_):
                global __rush_flags
                if __rush_flags or __hwnd is None:
                        return
                __rush_flags = True
                t = threading.Thread(target=__rush_voyage_thread, )
                t.setDaemon(True)
                t.start()

        comment = '抢 {0} 星流行'.format(hosi)
        return comment, __rush_voyage


def _rush_key(key_list, wait_time=0.05):
        def __rush_key_thread():
                while __rush_flags:
                        for x in key_list:
                                force.core.keyboard.input_key(x, __hwnd)
                                general.random_wait(wait_time)

        def __rush_key(_):
                global __rush_flags
                if __rush_flags:
                        return
                __rush_flags = True
                t = threading.Thread(target=__rush_key_thread, )
                t.setDaemon(True)
                t.start()

        comment = '连续 {0}'.format(key_list)
        return comment, __rush_key


def _clear_auction(which=1):
        def __clear_auction_thread():
                while __rush_flags:
                        # 不计算边框坐标, (x-1, y-26)
                        force.core.mouse.click('left', 405, 197, __hwnd, wait_time=.2)  # 搜索
                        general.random_wait()
                        force.core.mouse.click('left', 594, 260, __hwnd, wait_time=.2)  # 第 which 个
                        general.random_wait()
                        force.core.mouse.click('left', 994, 642, __hwnd, wait_time=.2)  # 购买
                        general.random_wait()
                        force.core.mouse.click('left', 662, 470, __hwnd, wait_time=.2)  # 数量
                        general.random_wait()
                        force.core.mouse.click('left', 597, 419, __hwnd, wait_time=.2)  # 确认
                        general.random_wait(.5)
                        force.core.mouse.click('left', 700, 418, __hwnd, wait_time=.2)  # 二次确认
                        general.random_wait()

        def __clear_auction(_):
                global __rush_flags
                if __rush_flags or __hwnd is None:
                        return
                __rush_flags = True
                t = threading.Thread(target=__clear_auction_thread, )
                t.setDaemon(True)
                t.start()

        return '扫拍卖', __clear_auction


def _rush_click():
        def __rush_click_thread():
                while __rush_flags:
                        if __hwnd is None:
                                force.core.mouse.real_click('left')
                        else:
                                force.core.mouse.click('left', __mouse_x, __mouse_y,
                                                       __hwnd, wait_time=.3)
                        general.random_wait()

        def __rush_click(_):
                global __rush_flags
                if __rush_flags:
                        return
                __rush_flags = True
                t = threading.Thread(target=__rush_click_thread, args=())
                t.setDaemon(True)
                t.start()

        return '连续左键', __rush_click
