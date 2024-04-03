import numpy as np
import config
import os
import time

saving_path = 'logs'
def resultSave(dif, cN, iN, ES):
    result = np.array([dif, cN,iN, ES])
    timestr = time.strftime("%Y%m%d-%H%M%S")
    savepath = os.path.join(config.SAVING_PATH, timestr + '.npy')
    
    np.save(savepath, result)