__all__ = ['wuxiaMapping']

from . import general_lib
from . import base


class _WuxiaMapping(base.BaseMapping):
        def __init__(self):
                super().__init__()
                self.MODE = 'wuxia'

        def press(self):
                return dict({
                        "#['Rshift', 'F10']": general_lib.switch_normal,
                }, **super().press())

        def release(self):
                return dict({}, **super().release())


wuxiaMapping = _WuxiaMapping()
