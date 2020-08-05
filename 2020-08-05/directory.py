# Unfinished. ran into some problems. WILL Research and come back to complete.

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/') if isfile(join('/home/', f))]

print(files_list)
