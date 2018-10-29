# coding=utf-8

import win32gui
import win32ui
from ctypes import windll
import math
from PIL import Image  # pillow
import setting


class Capture:
        def __init__(self):
                self.image = None

        def shot(self, hwnd=None):
                if hwnd is None:
                        hwnd = windll.user32.GetForegroundWindow()
                wdc = win32gui.GetWindowDC(hwnd)
                dc_obj = win32ui.CreateDCFromHandle(wdc)
                cdc = dc_obj.CreateCompatibleDC()

                left, top, right, bottom = win32gui.GetClientRect(hwnd)
                w = (right - left)
                h = (bottom - top)

                save_bit_map = win32ui.CreateBitmap()
                save_bit_map.CreateCompatibleBitmap(dc_obj, w, h)
                cdc.SelectObject(save_bit_map)
                if windll.user32.PrintWindow(hwnd, cdc.GetSafeHdc(), 1):
                        cdc.DeleteDC()
                        dc_obj.DeleteDC()
                        win32gui.ReleaseDC(hwnd, wdc)

                        bmp_info = save_bit_map.GetInfo()
                        bmp_bits = save_bit_map.GetBitmapBits(True)
                        win32gui.DeleteObject(save_bit_map.GetHandle())
                        self.image = Image.frombuffer('RGB',
                                                  (bmp_info['bmWidth'], bmp_info['bmHeight']),
                                                  bmp_bits, 'raw', 'BGRX', 0, 1)
                else:
                        if setting.INFO:
                                print('Can\'t get image!')
                        self.image = None

        def crop(self, left, top, right, bottom):
                self.image = self.image.crop((left, top, right, bottom))

        def similar(self, path):
                h_image_1 = self.image.histogram()
                h_image_2 = Image.open(path).histogram()
                return math.sqrt(sum(map(lambda a, b: (a - b) ** 2, h_image_1, h_image_2)) / len(h_image_1))

        def show(self):
                self.image.show()


if __name__ == '__main__':
        import time
        time.sleep(1)
        capture = Capture()
        capture.shot()
        capture.crop(100, 0, 200, 300)
        result = capture.similar('C:/Users/kakoi/Desktop/1/1.bmp')
        print(result)
        capture.show()
