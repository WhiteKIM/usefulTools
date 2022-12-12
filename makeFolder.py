import os
from queue import Empty
import shutil
import time

count = 0

PATH = os.path.dirname(os.path.abspath(__file__))
fileList = os.listdir('./')
start = time.time()
length =len(fileList)
index = 0

for (path, dir, files) in os.walk(PATH):
    for filename in files:
        if(index%2000==0):
            os.mkdir(str(count))
            count+=1
        shutil.move(filename, './'+str(count))
        index+=1
    