import sys
import PyQt5.QtWidgets
import PyQt5.QtQml
import PyQt5.QtGui

from listen.keyListen import keyListen
from interactive.qmlReceive import qmlReceive
from interactive import interactive
from simulator.mapping import mapping
import simulator.mode.normal


if __name__ == '__main__':
        keyListen.start()

        app = PyQt5.QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(PyQt5.QtGui.QIcon('main.ico'))
        engine = PyQt5.QtQml.QQmlApplicationEngine()
        context = engine.rootContext()
        mapping.mode_switch(simulator.mode.normal.normalMapping)
        con = interactive.Interactive()
        context.setContextProperty('con', con)
        engine.load('qml/main.qml')
        qmlReceive.set_root_object(engine.rootObjects()[0])
        qmlReceive.refresh_keylist()
        app.exec_()
