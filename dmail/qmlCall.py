# coding=utf-8

__all__ = ['QmlCall']

import PyQt5.QtCore
import exception


class QmlCall(object):
        def __init__(self):
                self.root_object = None

        def set_root_object(self, root_object) -> None:
                self.root_object = root_object

        @exception.general_exception(False)
        def refresh_keylist(self) -> bool:
                if self.root_object is None:
                        raise exception.ObjectException('root object not set!')
                PyQt5.QtCore.QMetaObject.invokeMethod(self.root_object, 'output_get',
                                                      PyQt5.QtCore.Qt.QueuedConnection)
                return True

        @exception.general_exception(False)
        def tray_info(self, title: str, content: str) -> bool:
                if self.root_object is None:
                        raise exception.ObjectException('root object not set!')
                PyQt5.QtCore.QMetaObject.invokeMethod(self.root_object, 'tray_info',
                                                      PyQt5.QtCore.Qt.DirectConnection,
                                                      PyQt5.QtCore.Q_ARG(PyQt5.QtCore.QVariant, title),
                                                      PyQt5.QtCore.Q_ARG(PyQt5.QtCore.QVariant, content))
                return True
