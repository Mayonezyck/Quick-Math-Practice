#result Analysis
#Fetch all results in the logs folder
import config
import os
import glob
def resultAna():	
	folder_path = config.SAVING_PATH# Replace with your folder's path
	npy_files = glob.glob(folder_path + "/*.npy")

	print(npy_files)