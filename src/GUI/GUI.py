import sys
from src.GUI.ButtonAction import openLogs
from src.ProbGen import probGen1
import time
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
    QFileDialog,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QWidget,
    QSlider
)
from PyQt6 import QtCore
import src.ResultR.resultSave as resultSave
import src.ResultR.resultAna as analyze
import config

#The first window that shows up
class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.w = config.WIDTH; self.h = config.HEIGHT
        self.resize(self.w,self.h)
        self.setWindowTitle("QMainWindow")
        self._createCentral()
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createCentral(self):
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
        self.difficulty = 0
        self.slider = QSlider(QtCore.Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(2)
        self.slider.setMaximumWidth(50)
        self.slider.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.slider.valueChanged.connect(self._update_dif_value)
        self.value_label = QLabel("0")
        self.value_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.value_label)
        self.setCentralWidget(centralwidget)

    def _createMenu(self):
        file = self.menuBar().addMenu("&File")
        #file.addAction("&Clear all", self._test)
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)
        logsMenu = self.menuBar().addMenu("&Log")
        logsMenu.addAction('&Open', self._open_logs)
        logsMenu.addAction('&Analyze', self._analyze_logs)
        
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
            self.new_window = SecondWindow(number, self.difficulty)
            self.new_window.show()
            print('smth')
        except ValueError:
            error_dialog = QMessageBox.warning(self, "Error", "Please enter a valid number.")
            self.status.showMessage('Error: invalid number input')
            self.setStatusBar(self.status)
    
    def _open_logs(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a File")
        openLogs.openLogs(file_path)
    def _analyze_logs(self):
        analyze.resultAna()
    def _update_dif_value(self, value):
        self.value_label.setText(str(value))
        self.difficulty = value
    

    
class SecondWindow(QWidget):
    def __init__(self, number, difficulty, mod = 'gen1'):
        super().__init__()
        self.Correct = 0
        self.InCorrect = 0
        self.setWindowTitle("Second Window")
        self.layout = QVBoxLayout(self)
        self.firstGo = True
        self.label = QLabel(f"You entered the number: {number}")
        self.difficulty = difficulty
        match mod:
            case 'gen1':
                self.ProbGen = probGen1.probGen1(number, self.difficulty)
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
        self.setFocus()

    
        self._show_next_item()
        self.preValue
        self.startTime = time.time()
        
            
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
            endTime = time.time()
            Elapseconds = endTime - self.startTime
            print(f'Correct: {self.Correct}, Incorrect: {self.InCorrect}')
            resultSave.resultSave(self.difficulty, self.Correct, self.InCorrect, Elapseconds)
            
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

