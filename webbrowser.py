# Python
import sys
import os
import logging
import traceback
logger = logging.getLogger()

# PyQt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl



class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        browser = QWebEngineView(parent=self)
        page = browser.setUrl(QUrl("http://web.de"))
        # browser.show()

        browser.resize(800, 600)
        self.resize(800, 600)


if __name__ == "__main__":
    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = "5588"
    app = QApplication(['--remote-debugging-port=5588'])

    window = BrowserWindow()
    window.show()

    sys.exit(app.exec())
