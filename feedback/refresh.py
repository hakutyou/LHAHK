__all__ = ['init', 'refresh']

import PyQt5.QtCore

__root_object = None


def init(root_object):
        global __root_object
        __root_object = root_object


def refresh():
        if __root_object is None:
                print('root object not set!')
                return
        output_object = __root_object.findChild(PyQt5.QtCore.QObject, 'resultRect')
        PyQt5.QtCore.QMetaObject.invokeMethod(output_object, 'output_get')
