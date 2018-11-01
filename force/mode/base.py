# coding=utf-8

__all__ = ['BaseMapping']


class BaseMapping(object):
        """
        Base: base function for every mode
        """
        def __init__(self):
                self.MODE = 'base'

        @property
        def press(self) -> dict:
                return {}

        @property
        def release(self) -> dict:
                return {}
