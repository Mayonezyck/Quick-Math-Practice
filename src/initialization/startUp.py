# This script gotta be called when the program starts:
# It should 
#   Check the log, create one if nothing exists
#   ...
import os
import numpy as np
def checkLogs(cwd):
    if not os.path.exists(os.path.join(cwd,'logs')):#create folder if ./log DNE
        print('Creating new log folder')
        os.makedirs(os.path.join(cwd,'logs'))