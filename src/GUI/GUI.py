import sys
from src.GUI.ButtonAction import test, newQuestions
# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QRadioButton,
    QPushButton,
    QFrame,
    QVBoxLayout,
    QWidget
)


class Window(QMainWindow):
    def __init__(self):
        self.w = 1280; self.h = 720
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        layout = QVBoxLayout()
        layout.addWidget(QFrame())
        layout.addWidget(QRadioButton(text='radio text'))
        layout.addWidget(QPushButton(text='push button text'))
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.resize(self.w,self.h)
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
    
    def _oneRound(self):
        pass
        #Take the number of exercises first.
        #Generate a random seed
        #Generate random exercises based on the random seed.
        #Generate 
    
def app():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

