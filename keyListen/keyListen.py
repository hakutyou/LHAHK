__all__ = ['KeyListen']

from ctypes import *
from functools import partial
import PyHook3 as pyHook
import threading


class KeyListen:
        def __init__(self, press_mapping, release_mapping, debug=False):
                self.debug = debug

                self.hold_key = []
                self.prev_state = True
                self.press_mapping = press_mapping
                self.release_mapping = release_mapping
                hm = pyHook.HookManager()
                on_key_down = partial(self.on_key_response, response=True)
                on_key_up = partial(self.on_key_response, response=False)
                hm.KeyDown = on_key_down
                hm.KeyUp = on_key_up
                hm.HookKeyboard()

        def on_key_response(self, event, response):
                if response and event.Key in self.hold_key:
                        return self.prev_state
                win_title = create_string_buffer(512)
                windll.user32.GetWindowTextA(event.Window, byref(win_title), 512)
                window_name = win_title.value.decode('gbk')
                if self.debug:
                        print('正处于"{0}"窗口'.format(window_name))

                if response:
                        self.hold_key.append(event.Key)
                        hold_key_str = str(self.hold_key)
                        if hold_key_str in self.press_mapping:
                                t = threading.Thread(
                                        target=self.press_mapping[hold_key_str],
                                        args=(window_name,))
                                t.start()
                                self.prev_state = False
                                return False
                        if self.debug:
                                print('刚刚按下了"{0}"键'.format(self.hold_key))
                else:
                        self.hold_key.remove(event.Key)
                        hold_key_str = str(self.hold_key)
                        if hold_key_str in self.release_mapping:
                                t = threading.Thread(
                                        target=self.release_mapping[hold_key_str],
                                        args=(window_name,))
                                t.start()
                                self.prev_state = False
                                return False
                        if self.debug:
                                print('刚刚抬起了"{0}"键, {1}'.format(
                                        event.Key, self.hold_key))
                self.prev_state = True
                return True
