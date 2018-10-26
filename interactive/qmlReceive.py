__all__ = ['QmlReceive']

import PyQt5.QtCore

from simulator.mapping import mapping


class QmlReceive(PyQt5.QtCore.QObject):
        def __init__(self, parent=None):
                super(QmlReceive, self).__init__(parent)

        @PyQt5.QtCore.pyqtSlot(result=list)
        def get_key_list(self):
                mapper = mapping.press_mapping
                return list(map(lambda x: {'doc': mapper[x][0],
                                           'hotkey': x},
                                mapper))
                # return [{'role_name': '读取失败'}]

        @PyQt5.QtCore.pyqtSlot(result=str)
        def get_mode(self):
                return mapping.mode

        @PyQt5.QtCore.pyqtSlot(str)
        def output(self, string):
                print(string)
