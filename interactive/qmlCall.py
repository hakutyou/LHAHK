__all__ = ['QmlCall']

import PyQt5.QtCore


class QmlCall:
        def __init__(self):
                self.root_object = None

        def set_root_object(self, root_object):
                self.root_object = root_object

        def refresh_keylist(self):
                if self.root_object is None:
                        print('root object not set!')
                        return
                PyQt5.QtCore.QMetaObject.invokeMethod(self.root_object, 'output_get',
                                                      PyQt5.QtCore.Qt.QueuedConnection)

        def tray_info(self, title, content):
                if self.root_object is None:
                        print('root object not set!')
                        return
                PyQt5.QtCore.QMetaObject.invokeMethod(self.root_object, 'tray_info',
                                                      PyQt5.QtCore.Qt.DirectConnection,
                                                      PyQt5.QtCore.Q_ARG(PyQt5.QtCore.QVariant, title),
                                                      PyQt5.QtCore.Q_ARG(PyQt5.QtCore.QVariant, content))
