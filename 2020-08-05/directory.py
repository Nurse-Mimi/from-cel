import os, fnmatch

files_list = os.listdir('.')
pattern = "*.py"

for entry in files_list:
    if fnmatch.fnmatch(entry, pattern):
        print(entry)
