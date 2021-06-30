import os
import re
import pathlib

# Get current directory
# print (pathlib.Path.cwd())

current = pathlib.Path.cwd()

for dirpath, dirnames, filenames in os.walk(current):
    for dirname in dirnames:
        #for filename in filenames:
        # print (dirname)
        # print(dirpath)
            #if filename == "20170412":
        
        for results in re.finditer("Time\sLapse\s\d+", dirname):
            print(results.group(0))
        