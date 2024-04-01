import os
import sys
from src.initialization import *
from src.GUI import GUI

#StartUp and Prep
startUp.checkLogs(os.getcwd())


#StartUp GUI
GUI.app()