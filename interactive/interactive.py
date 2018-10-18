__all__ = ['Interactive']

import PyQt5.QtCore


class Interactive(PyQt5.QtCore.QObject):
        def __init__(self, simulator, parent=None):
                super(Interactive, self).__init__(parent)
                self.simulator = simulator

        @PyQt5.QtCore.pyqtSlot(result=list)
        def get_key_list(self):
                mapping = self.simulator.press_mapping
                return list(map(lambda x: {'role_id': mapping[x].__doc__,
                                           'role_name': x},
                                mapping))
                # return [{'role_name': '读取失败'}]

        @PyQt5.QtCore.pyqtSlot(str)
        def output(self, string):
                print(string)
