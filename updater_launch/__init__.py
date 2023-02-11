from __future__ import annotations

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtProperty, pyqtSignal, pyqtSlot
from pyupdater.client import Client, AppUpdate
from client_config import ClientConfig
from .version import VERSION


class DownloadingApp(QtCore.QThread):
    def __init__(self):
        super().__init__()
        self._update = None

    def set_update(self, upd: AppUpdate):
        self._update = upd

    def run(self) -> None:
        self._update.download()


class UpdaterLaunch(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(2 * 1000)
        self.timer.timeout.connect(self.check_update)
        self.timer.start()
        self._client = Client(ClientConfig())

        self._update: AppUpdate | None = None
        self._has_update = False

        self._downloader = DownloadingApp()
        self._downloader.finished.connect(self.extract)

    signalVersion = pyqtSignal()

    @pyqtProperty(str, notify=signalVersion)
    def version(self):
        return VERSION

    @pyqtSlot()
    def updating(self):
        assert self._update
        self._downloader.set_update(self._update)
        self._downloader.start()

    def extract(self):
        if self._update.is_downloaded():
            self._update.extract_restart()

    signalHasUpdate = pyqtSignal()

    @pyqtProperty(bool, notify=signalHasUpdate)
    def has_update(self):
        return bool(self._update)

    @has_update.setter
    def has_update(self, v: bool):
        self._has_update = v
        self.signalHasUpdate.emit()

    def _check_updating_process(self):
        if self._has_update:
            self.timer.stop()
        else:
            self.timer.start()

    def check_update(self):
        try:
            self._client.refresh()
            self._update = self._client.update_check(ClientConfig.APP_NAME, VERSION)
            self.has_update = bool(self._update)
        except Exception as e:
            print(e)
