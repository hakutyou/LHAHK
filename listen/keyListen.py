__all__ = ['keyListen']

from ctypes import *
from functools import partial
import PyHook3 as pyHook
import threading
import copy
from interactive.setting import DEBUG

from simulator.mapping import mapping
from simulator.core import keyboardGlob


class _KeyListen:
        def __init__(self):
                self._new_key = 0
                self.press_key = []

        def start(self):
                hm = pyHook.HookManager()
                on_key_down = partial(self.on_key_response, response=True)
                on_key_up = partial(self.on_key_response, response=False)
                hm.KeyDown = on_key_down
                hm.KeyUp = on_key_up
                hm.HookKeyboard()

        def on_key_response(self, event, response):
                if self.is_lock():
                        return True
                # if response and event.Key in self.hold_key:
                #         return self.prev_state
                if DEBUG:
                        win_title = create_string_buffer(512)
                        windll.user32.GetWindowTextA(event.Window, byref(win_title), 512)
                        window_name = win_title.value.decode('gbk')
                        print('正处于"{0}"窗口'.format(window_name))

                # new_key = True
                hold_key_str_l = event.Key
                if response:
                        if event.Key not in self.press_key:
                                self._new_key = 0
                                self.press_key.append(event.Key)
                                if DEBUG:
                                        print('刚刚按下了"{0}"键'.format(self.press_key))
                        else:
                                # if self._new_key == 0:
                                #         self.press_key.append('*')
                                self._new_key += 1
                        mapper = mapping.press_mapping
                        hold_key_lst = self.press_key
                else:
                        self._new_key = 0
                        mapper = mapping.release_mapping
                        hold_key_lst = copy.deepcopy(self.press_key)
                        if event.Key in self.press_key:
                                if DEBUG:
                                        print('刚刚抬起了"{0}"键, {1}'.format(
                                                event.Key, self.press_key))
                                p = self.press_key.index(event.Key)
                                # try:
                                #         if self.press_key[p+1] == '*':
                                #                 self.press_key.pop(p+1)
                                # except IndexError:
                                #         pass
                                self.press_key.pop(p)

                _target = ''
                hold_key_str = str(hold_key_lst)
                if hold_key_str in mapper:            # normal mode
                        _target = hold_key_str
                elif '#' + hold_key_str in mapper:    # just response once
                        if self._new_key == 0:
                                _target = '#' + hold_key_str
                # elif '$' + hold_key_str in mode:    # just response when hold on
                #         if self._new_key == 1:
                #                 _target = '$' + hold_key_str
                elif '*' + hold_key_str_l in mapper:  # must be at last
                        _target = '*' + hold_key_str_l

                if _target:
                        t = threading.Thread(target=mapper[_target],
                                             args=(event.Window,))
                        t.start()
                        return False
                return True

        @staticmethod
        def is_lock():
                return keyboardGlob.is_lock()


keyListen = _KeyListen()
