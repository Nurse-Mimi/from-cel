from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/2020-08-05') if isfile(join('/home/2020-08-05', f))]

print(files_list)
