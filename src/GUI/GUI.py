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
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
    QWidget,
)


class Window(QMainWindow):
    def __init__(self):
        self.w = 1280; self.h = 720
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.layout = QVBoxLayout()
        self.textbox = QLineEdit()
        self.layout.addWidget(self.textbox)

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self._open_new_window)
        self.layout.addWidget(self.button)
        centralwidget = QWidget()
        centralwidget.setLayout(self.layout)
        self.setCentralWidget(centralwidget)
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
    
    def _open_new_window(self):
        try:
            number = int(self.textbox.text())
            self.new_window = SecondWindow(number)
            self.new_window.show()
        except ValueError:
            error_dialog = QMessageBox.warning(self, "Error", "Please enter a valid number.")
    
    def _test(self):
        test.test()
    
    def _oneRound(self):
        pass
        #Take the number of exercises first.
        #Generate a random seed
        #Generate random exercises based on the random seed.
        #Generate 
    
class SecondWindow(QWidget):
    def __init__(self, number):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.layout = QVBoxLayout(self)

        self.label = QLabel(f"You entered the number: {number}")
        self.layout.addWidget(self.label)

def app():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

