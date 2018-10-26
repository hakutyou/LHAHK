__all__ = ['KeyListen']

import threading
from ctypes import *
from functools import partial
import PyHook3 as pyHook
import simulator.core
import setting

from simulator.mapping import mapping


class KeyListen:
        def __init__(self):
                self.__hold_key = 0
                self.pressed_key = []

        def start(self):
                hm = pyHook.HookManager()
                on_key_down = partial(self.on_key_response, state=True)
                on_key_up = partial(self.on_key_response, state=False)
                hm.KeyDown = on_key_down
                hm.KeyUp = on_key_up
                hm.HookKeyboard()

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
                if hold_key_str in mapper:            # normal mode
                        _target = hold_key_str
                elif '#' + hold_key_str in mapper:    # just response once
                        if self.__hold_key == 0:
                                _target = '#' + hold_key_str
                # elif '$' + hold_key_str in mode:    # just response when hold on
                #         if self._new_key == 1:
                #                 _target = '$' + hold_key_str
                elif '*' + hold_key_str_l in mapper:  # must be at last
                        _target = '*' + hold_key_str_l

                if _target:
                        t = threading.Thread(target=mapper[_target][1],
                                             args=(event.Window,))
                        t.start()
                        return False
                return True

        @property
        def is_lock(self):
                return simulator.core.keyboard.is_lock()
