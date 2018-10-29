# coding=utf-8

__all__ = ['Readfile']

import ast
import setting


class Readfile:
        def __init__(self, filename: str = None):
                self.filename = filename
                self.__value = None

        def set_filename(self, filename: str):
                self.filename = filename
                self.__value = None

        @property
        def value(self):
                if self.filename is None:
                        if setting.DEBUG:
                                print('not setting filename')
                if self.__value is not None:
                        return self.__value
                if setting.DEBUG:
                        print('readfile evaluate')
                try:
                        self.__value = ast.literal_eval(open(self.filename, 'r').read())
                        return self.__value
                except SyntaxError:
                        if setting.INFO:
                                print('extern file syntax: {0}'.format(self.filename))
                        return {}
                except FileNotFoundError:
                        if setting.DEBUG:
                                print('no such file: {0}'.format(self.filename))
                        return {}
