# coding=utf-8

__all__ = ['KeyListen']

import threading
from ctypes import *
from functools import partial
import PyHook3 as pyHook
import simulator.core
import setting

from simulator.mapping import mapping

MACS = {
        'Lshift':   0o0001,
        'Rshift':   0o0002,
        'Shift':    0o0004,
        'Lcontrol': 0o0010,
        'Rcontrol': 0o0020,
        'Control':  0o0040,
        'Lmenu':    0o0100,
        'Rmenu':    0o0200,
        'Menu':     0o0400,
        'Lwin':     0o1000,
        'Rwin':     0o2000,
        'Win':      0o4000,
}


class KeyListen(object):
        def __init__(self):
                self.__hold_key = 0
                self.pressed_key = []
                self.macs = 0x00

        def start(self):
                hm = pyHook.HookManager()
                on_key_down = partial(self.on_key_response, state=True)
                on_key_up = partial(self.on_key_response, state=False)
                hm.KeyDown = on_key_down
                hm.KeyUp = on_key_up
                hm.HookKeyboard()

        @staticmethod
        def macs_record(key):
                if key in MACS:
                        return MACS[key]
                return 0

        def macs_extend(self):
                maybe = ['']
                for i in '{0:04o}'.format(self.macs):
                        if i == '1' or i == '2':
                                maybe = list(map(lambda x: x+i, maybe)) +\
                                        list(map(lambda x: x+'3', maybe))
                        else:
                                maybe = list(map(lambda x: x+i, maybe))
                return maybe + ['']

        def on_key_response(self, event, state):
                if self.is_lock:
                        return True
                # if response and event.Key in self.hold_key:
                #         return self.prev_state
                if setting.DEBUG:
                        win_title = create_string_buffer(512)
                        windll.user32.GetWindowTextA(event.Window, byref(win_title), 512)
                        window_name = win_title.value.decode('gbk')
                        print('正处于"{0}"窗口'.format(window_name))

                # new_key = True
                hold_key_str_l = event.Key
                if state:               # press
                        if setting.MACS:
                                _macs = self.macs_record(event.Key)
                                if _macs != 0:
                                        self.macs |= _macs
                                        if setting.DEBUG:
                                                print('state = {0}'.format(self.macs))
                                        return True
                        if event.Key not in self.pressed_key:
                                self.__hold_key = 0
                                self.pressed_key.append(event.Key)
                                if setting.DEBUG:
                                        print('刚刚按下了"{0}"键, {1}'.format(
                                                event.Key, self.pressed_key))
                        else:
                                self.__hold_key += 1
                        mapper = mapping.press_mapping
                        hold_key_str = str(self.pressed_key)
                else:                   # release
                        if setting.MACS:
                                _macs = self.macs_record(event.Key)
                                if _macs != 0:
                                        self.macs &= ~_macs
                                        if setting.DEBUG:
                                                print('state = {0}'.format(self.macs))
                                        return True
                        self.__hold_key = 0
                        mapper = mapping.release_mapping
                        hold_key_str = str(self.pressed_key)
                        if event.Key in self.pressed_key:
                                if setting.DEBUG:
                                        print('刚刚抬起了"{0}"键, {1}'.format(
                                                event.Key, self.pressed_key))
                                p = self.pressed_key.index(event.Key)
                                self.pressed_key.pop(p)

                _target = ''
                for x in self.macs_extend():
                        if x + hold_key_str in mapper:
                                _target = x + hold_key_str
                                break
                        if x + '#' + hold_key_str in mapper:
                                if self.__hold_key == 0:
                                        _target = x + '#' + hold_key_str
                                        break
                        if x + '*' + hold_key_str_l in mapper:
                                _target = x + '*' + hold_key_str_l

                if _target:
                        t = threading.Thread(target=mapper[_target][1],
                                             args=(event.Window,))
                        t.start()
                        return False
                return True

        @property
        def is_lock(self):
                return simulator.core.keyboard.is_lock()
