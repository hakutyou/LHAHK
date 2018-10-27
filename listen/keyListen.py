__all__ = ['KeyListen']

import threading
from ctypes import *
from functools import partial
import PyHook3 as pyHook
import simulator.core
import setting

from simulator.mapping import mapping

LShift = 0x01
RShift = 0x02
Shift = 0x03
LControl = 0x04
RControl = 0x08
Control = 0x0c
LMenu = 0x10
RMenu = 0x20
Meta = 0x30
LWin = 0x40
RWin = 0x80
Win = 0xc0


class KeyListen:
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
                if key == 'Lshift':
                        return LShift
                elif key == 'Rshift':
                        return RShift
                elif key == 'Lmenu':
                        return LMenu
                elif key == 'Rmenu':
                        return RMenu
                elif key == 'Lcontrol':
                        return LControl
                elif key == 'Rcontrol':
                        return RControl
                elif key == 'Lwin':
                        return LWin
                elif key == 'Rwin':
                        return RWin
                return 0

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
                for x in [str(self.macs), '']:
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
