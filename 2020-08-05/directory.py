import os

folder_path ='C\Users\HP\Desktop\from-cel'

def listdir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print("File name: " + fileName)
        print('Folder Path: ' + os.path.abspath(os.path.join(dir, fileName)), sep='\n')
