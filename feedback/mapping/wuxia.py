__all__ = ['wuxiaMapping']

from ..base import mapping
from .. import simulation

from . import base
from . import normal


class _WuxiaMapping(base.BaseMapping):
        def __init__(self):
                super().__init__()
                self.MODE = 'wuxia'

        def press(self):
                return dict({
                        "#['Rshift', 'F10']": lambda _: mapping.mode_switch(
                                normal.normalMapping),
                }, **super().press())

        def release(self):
                return dict({}, **super().press())


wuxiaMapping = _WuxiaMapping()
