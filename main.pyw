# coding=utf-8

import sys
import PyQt5.QtWidgets
import PyQt5.QtQml
import PyQt5.QtGui

import dmail
import kala
from force.mapping import mapping
from force.mode.normal import normalMapping


if __name__ == '__main__':
        app = PyQt5.QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(PyQt5.QtGui.QIcon('main.ico'))
        engine = PyQt5.QtQml.QQmlApplicationEngine()
        context = engine.rootContext()

        kala.keyListener.start()
        mapping.mode_switch(normalMapping)
        context.setContextProperty('externer', dmail.qmlReceiver)
        engine.load('qml/main.qml')
        dmail.qmlCaller.set_root_object(engine.rootObjects()[0])
        dmail.qmlCaller.refresh_keylist()

        app.exec_()
