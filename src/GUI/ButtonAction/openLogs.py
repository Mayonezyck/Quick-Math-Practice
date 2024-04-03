import numpy as np
import config
import os
def openLogs(filePath):
    log = np.load(filePath)

    print(log)