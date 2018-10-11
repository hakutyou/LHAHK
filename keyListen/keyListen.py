__all__ = ['KeyListen']

from ctypes import *
from functools import partial
import PyHook3 as pyHook
import threading


class KeyListen:
        def __init__(self, press_mapping, release_mapping, locker, debug=False):
                self.debug = debug

                self.press_key = []
                self.press_mapping = press_mapping
                self.release_mapping = release_mapping
                self.locker = locker
                hm = pyHook.HookManager()
                on_key_down = partial(self.on_key_response, response=True)
                on_key_up = partial(self.on_key_response, response=False)
                hm.KeyDown = on_key_down
                hm.KeyUp = on_key_up
                hm.HookKeyboard()

        def on_key_response(self, event, response):
                if self.locker.is_lock():
                        return True
                # if response and event.Key in self.hold_key:
                #         return self.prev_state
                win_title = create_string_buffer(512)
                windll.user32.GetWindowTextA(event.Window, byref(win_title), 512)
                window_name = win_title.value.decode('gbk')
                if self.debug:
                        print('正处于"{0}"窗口'.format(window_name))

                new_key = False
                if event.Key not in self.press_key:
                        self.press_key.append(event.Key)
                        new_key = True
                hold_key_str = str(self.press_key)
                if response:
                        if new_key and self.debug:
                                print('刚刚按下了"{0}"键'.format(self.press_key))
                        mapping = self.press_mapping
                else:
                        if new_key and self.debug:
                                print('刚刚抬起了"{0}"键, {1}'.format(
                                        event.Key, self.press_key))
                        mapping = self.release_mapping

                _target = ''
                if hold_key_str in mapping:
                        _target = hold_key_str
                elif '#' + hold_key_str in mapping:
                        if new_key:
                                _target = '#' + hold_key_str
                        else:
                                return False

                if _target:
                        t = threading.Thread(target=mapping[_target],
                                             args=(window_name,))
                        t.start()
                        return False
                return True
