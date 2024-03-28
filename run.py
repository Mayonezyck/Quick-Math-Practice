import os

from src.initialization import *
from src.GUI import *

#StartUp and Prep
startUp.checkLogs(os.getcwd())


#StartUp GUI
GUI.app()