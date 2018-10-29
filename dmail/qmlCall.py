# coding=utf-8

__all__ = ['QmlCall']

import PyQt5.QtCore
import setting


class QmlCall(object):
        def __init__(self):
                self.root_object = None

        def set_root_object(self, root_object):
                self.root_object = root_object

        def refresh_keylist(self) -> bool:
                if self.root_object is None:
                        if setting.INFO:
                                print('root object not set!')
                        return False
                PyQt5.QtCore.QMetaObject.invokeMethod(self.root_object, 'output_get',
                                                      PyQt5.QtCore.Qt.QueuedConnection)
                return True

        def tray_info(self, title: str, content: str) -> bool:
                if self.root_object is None:
                        if setting.INFO is None:
                                print('root object not set!')
                        return False
                PyQt5.QtCore.QMetaObject.invokeMethod(self.root_object, 'tray_info',
                                                      PyQt5.QtCore.Qt.DirectConnection,
                                                      PyQt5.QtCore.Q_ARG(PyQt5.QtCore.QVariant, title),
                                                      PyQt5.QtCore.Q_ARG(PyQt5.QtCore.QVariant, content))
                return True
