import sys
from src.GUI.ButtonAction import test
from src.ProbGen import probGen1
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
    QHBoxLayout,
    QMessageBox,
    QWidget,
)
from PyQt6 import QtCore
import src.ResultR.resultSave as resultSave

#The first window that shows up
class Window(QMainWindow):
    def __init__(self):
        self.w = 1280; self.h = 720
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
        bigTitle = QLabel(text='Calculation Practice')
        bigTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        bigTitle.setStyleSheet("QLabel { font-size: 60pt; }") 
        self.layout.addWidget(bigTitle)
        input_row_layout = QHBoxLayout()
        input_row_layout.addWidget(QLabel(text='Number of practices'))
        self.textbox = QLineEdit()
        self.textbox.setMaximumWidth(30)
        input_row_layout.addWidget(self.textbox)
        input_row_layout.setContentsMargins(600, 0, 600, 0)
        self.layout.addLayout(input_row_layout)
        self.button = QPushButton("Submit")
        self.button.setDefault(True)
        self.button.clicked.connect(self._open_new_window)
        self.layout.addWidget(self.button)
        centralwidget = QWidget()
        #centralwidget.setStyleSheet("background-color: lightgray;")  # Optional styling
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
        self.status = QStatusBar()
        self.status.showMessage("Ready")
        self.setStatusBar(self.status)
    
    def _open_new_window(self):
        try:
            number = int(self.textbox.text())
            self.new_window = SecondWindow(number)
            self.new_window.show()
            print('smth')
        except ValueError:
            error_dialog = QMessageBox.warning(self, "Error", "Please enter a valid number.")
            self.status.showMessage('Error: invalid number input')
            self.setStatusBar(self.status)
    
    def _test(self):
        test.test()
    

    
class SecondWindow(QWidget):
    def __init__(self, number, mod = 'gen1'):
        super().__init__()
        self.Correct = 0
        self.InCorrect = 0
        self.setWindowTitle("Second Window")
        self.layout = QVBoxLayout(self)
        self.firstGo = True
        self.label = QLabel(f"You entered the number: {number}")
        match mod:
            case 'gen1':
                self.ProbGen = probGen1.probGen1(number)
        QuestionDic = self.ProbGen._generateQuestions()
        self.layout.addWidget(self.label)
        self.QuestionDicIt = iter(QuestionDic.items())
        self.QuestionLabel = QLabel('----')
        self.layout.addWidget(self.QuestionLabel)
        self.AnswerBox = QLineEdit()
        self.layout.addWidget(self.AnswerBox)
        self.nextButton = QPushButton(text='Next')
        self.nextButton.setDefault(True)
        self.nextButton.clicked.connect(self._show_next_item)
        self.layout.addWidget(self.nextButton)
        self._show_next_item()
        self.preValue
        

            
    def _show_next_item(self):
        try:
            if not self.firstGo:
                ans = int(self.AnswerBox.text())
                self._checkTF(ans,self.preValue)
                key, self.preValue = next(self.QuestionDicIt)
                self.QuestionLabel.setText(str(key))
                self.AnswerBox.setText('')
                self.AnswerBox.setFocus()
            else:
                self.firstGo = False
                key, self.preValue = next(self.QuestionDicIt)
                self.QuestionLabel.setText(str(key))
                
                
        except StopIteration:
            # Reached the end
            print(int(self.AnswerBox.text()))
            self.nextButton.setEnabled(False)
            self.firstGo = True
            self.QuestionLabel.setText("End of dictionary")
            self.AnswerBox.setDisabled(True)
            print(f'Correct: {self.Correct}, Incorrect: {self.InCorrect}')
            resultSave.resultSave(self.Correct, self.InCorrect)
            
        except ValueError:
            print('value error')
            
    def _checkTF(self, v1, v2):
        print(v1, v2)
        if v1 == v2:
            self.Correct += 1
        else:
            self.InCorrect += 1


def app():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

