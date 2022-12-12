import cv2
import numpy as np
import glob
import re


img_array = []
numbers = re.compile(r'(\d+)')
height =0 
width = 0

def numbericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

for filename in sorted(glob.glob('./*.png'), key=numbericalSort):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    img_array.append(img)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, (width,height))
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()