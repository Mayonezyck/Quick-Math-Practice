import numpy as np
import params
import os
def openLogs(filePath):
    log = np.load(filePath)

    print(log)