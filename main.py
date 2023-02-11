import os
import sys

# indicate it is bundle or source code
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


from PyQt6 import QtCore, QtWidgets, QtQml
from updater_launch import UpdaterLaunch
import logging

formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")


def setup_logging():
    logger = logging.getLogger()
    handler_stdout = logging.StreamHandler(stream=sys.stdout)
    handler_stdout.setFormatter(formatter)
    logger.addHandler(handler_stdout)
    logger.setLevel(logging.DEBUG)


def main():
    setup_logging()
    app = QtWidgets.QApplication([])
    engine = QtQml.QQmlApplicationEngine()
    updater = UpdaterLaunch()
    context = engine.rootContext()
    context.setContextProperty("updater", updater)
    engine.load(QtCore.QUrl.fromLocalFile("./App.qml"))
    app.exec()


if __name__ == '__main__':
    main()
