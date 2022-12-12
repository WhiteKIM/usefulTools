import json
import os
from collections import OrderedDict

'''
사용방법
1. labelme로 객체가 더이상 움직이지 않을 경우까지만 잡아준다
2. 코드를 이미지가 있는 폴더 안에 위치시킨다
3. run
4. labelme로 코드가 잘 작동되었는지 확인한다
5. finish
'''

def POP(list):
    list_len = len(list)
    result = list[list_len-1]
    return result

fileList = os.listdir('./')
img_list= []
json_list = []
json_file = ''

print('Enter the IMG File name: ', end='')
Input = input()

for file in fileList:
    if(file.endswith('.json')):
        json_list.append(os.path.splitext(file)[0])
    elif(file.endswith('.png')):
        img_list.append(os.path.splitext(file)[0])

temp = sorted(img_list,key=lambda img_num: int(img_num))
img_list = temp

temp2 = sorted(json_list,key=lambda json_num: int(json_num))
json_list = temp2

json_file = POP(json_list)+'.json'
with open(json_file,'r') as f:
    jsonData = json.load(f)
    json_version = jsonData['version']
    json_flags = jsonData['flags']
    json_shape = jsonData['shapes']
    json_imgData = jsonData['imageData']
    img_height = jsonData['imageHeight']
    img_width = jsonData['imageWidth']

start = img_list.index(Input)
for img_num in range(start,len(img_list)):
    img = img_list[img_num]
    if img not in json_list:
        fileData = OrderedDict()
        fileData['version'] = json_version
        fileData['flags'] = json_flags
        fileData['shapes'] = json_shape
        fileData['imagePath'] = img+'.png'
        fileData['imageData'] = None  #json_imgData
        fileData['imageHeight'] = img_height
        fileData['imageWidth'] = img_width
        jsonName = os.path.splitext(img)[0]+'.json'
        with open(jsonName, 'w') as makeJson:
            json.dump(fileData, makeJson, ensure_ascii=False, indent='\t')
            makeJson.close()
