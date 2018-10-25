__all__ = ['Interactive']

import PyQt5.QtCore

from simulator.mapping import mapping


class Interactive(PyQt5.QtCore.QObject):
        def __init__(self, parent=None):
                super(Interactive, self).__init__(parent)

        @PyQt5.QtCore.pyqtSlot(result=list)
        def get_key_list(self):
                mapper = mapping.press_mapping
                return list(map(lambda x: {'role_id': mapper[x].__doc__,
                                           'role_name': x},
                                mapper))
                # return [{'role_name': '读取失败'}]

        @PyQt5.QtCore.pyqtSlot(str)
        def output(self, string):
                print(string)

        @PyQt5.QtCore.pyqtSlot(result=str)
        def get_mode(self):
                return mapping.mode()
