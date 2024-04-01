import sys
from src.GUI.ButtonAction import test
# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        file = self.menuBar().addMenu("&File")
        file.addAction("&Clear all", self._test)
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)
        

    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)
    
    def _test(self):
        test.test()

def app():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

