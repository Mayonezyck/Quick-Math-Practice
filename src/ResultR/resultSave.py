import numpy as np
import params
import os
import time

saving_path = 'logs'
def resultSave(cN, iN):
    result = np.array([cN,iN])
    timestr = time.strftime("%Y%m%d-%H%M%S")
    savepath = os.path.join(params.SAVING_PATH, timestr + '.npy')
    
    np.save(savepath, result)