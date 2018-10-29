# coding=utf-8

__all__ = ['QmlReceive']

import PyQt5.QtCore

from force.mapping import mapping


class QmlReceive(PyQt5.QtCore.QObject):
        def __init__(self, parent=None):
                super(__class__, self).__init__(parent)

        @PyQt5.QtCore.pyqtSlot(result=list, name='get_key_list')
        def get_key_list(self) -> list:
                mapper = mapping.press_mapping
                return list(map(lambda x: {'doc': mapper[x][0],
                                           'hotkey': x},
                                mapper))

        @PyQt5.QtCore.pyqtSlot(result=str, name='get_mode')
        def get_mode(self) -> str:
                return mapping.mode

        @PyQt5.QtCore.pyqtSlot(str, name='output')
        def output(self, string: str) -> None:
                print(string)
