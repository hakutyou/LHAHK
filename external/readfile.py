# coding=utf-8

__all__ = ['Readfile']

import ast
import setting
import exception


class Readfile:
        def __init__(self, filename: str = None):
                self.filename = filename
                self.__value = None

        def set_filename(self, filename: str) -> None:
                self.filename = filename
                self.__value = None

        @property
        @exception.general_exception({})
        def value(self) -> dict:
                if self.filename is None:
                        raise exception.PathException('not setting filename', False)
                if self.__value is not None:
                        return self.__value
                if setting.DEBUG:
                        print('readfile evaluate')

                try:
                        self.__value = ast.literal_eval(open(self.filename, 'r').read())
                        return self.__value
                except SyntaxError:
                        raise exception.PathException('error file syntax: {path}'.format(path=self.filename))
                except FileNotFoundError:
                        raise exception.PathException('no such file: {path}'.format(path=self.filename))
