import sys
import PyQt5.QtWidgets
import PyQt5.QtQml
import PyQt5.QtCore

import listen.keyListen as keyListen
import feedback.keyFeedback as keyFeedback
import interactive.interactive as interactive
import feedback.refresh as refresh

debug = False


def simulator():
        key_holder = keyFeedback.init()
        listen = keyListen.KeyListen(keyFeedback.PRESS_MAPPING,
                                     keyFeedback.RELEASE_MAPPING,
                                     key_holder.hold_lock,
                                     debug=debug)
        return listen


if __name__ == '__main__':
        app = PyQt5.QtWidgets.QApplication(sys.argv)
        engine = PyQt5.QtQml.QQmlApplicationEngine()
        context = engine.rootContext()
        con = interactive.Interactive(simulator())
        context.setContextProperty('con', con)
        engine.load('qml/main.qml')
        refresh.init(engine.rootObjects()[0])
        refresh.refresh()
        app.exec_()
