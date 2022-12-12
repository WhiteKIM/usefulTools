from __future__ import annotations
import json
import os
from collections import OrderedDict
from tkinter import image_names

savePath = './save/'

label_list = []
"""
# 폴리곤 형태일 경우에 사용
# 폴리곤 형태를 박스형으로 변경
# 박스 형태의 두 좌표는 폴리곤에서 최상단 좌표 두개, 최하단 좌표값 두개를 이용
# 인자값 json파일, 반환 X
"""
def convCo2labelmePoly(jsonString):
    bBox = []
    max_x = 0
    max_y = 0
    min_x = 100000000000
    min_y = 100000000000
    data_poly = jsonString['polygon']
    data_class = jsonString['class']
    if(data_class=='05'):#05는 구름, 현재 사용치 않음
        return
    else:#01,02,03는 색이 다른 연기
        if(data_class=='01' or data_class=='02' or data_class=='03'):
            classname = 'smoke'
        elif(data_class=='04'):
            classname= 'fire'
        else:# 그외의 클래스가 존재함
            return
    for poly_index in range(len(data_poly)):
        data_poly_points = data_poly[poly_index]
        for index in range(len(data_poly_points)):
            num = data_poly_points[index]
            if(index==0 or index %2==0):    #x축
                if(num > max_x):
                    max_x = num
                if(num < min_x):
                    min_x = num
            else:   #y축
                if(num > max_y):
                    max_y = num
                if(num < min_y):
                    min_y = num   
    bBox.append([max_x, max_y])
    bBox.append([min_x, min_y])
    json_object ={
            "label":classname,#위에서 설정한 라벨명
            "points":bBox,#좌표값
            "group_id":None,#그룹아이디는 따로 설정하지 않음
            "shape_type":"rectangle",#사각형
            "flags":{}
    }
    return json_object
        
"""
# 사각형 형태일 경우에 사용
# 인자값 json파일, 반환 X
"""
def convCo2labelme(jsonString):
    bBox = []
    max_x = 0
    max_y = 0
    min_x = 100000000000
    min_y = 100000000000
    data_box = jsonString['box']
    data_class = jsonString['class']
    if(data_class=='05'):
        return
    else:
        if(data_class=='01' or data_class=='02' or data_class=='03'):
            classname = 'smoke'
        elif(data_class=='04'):
            classname= 'fire'
        else:
            return
    for box_index in range(len(data_box)):
        data_box_points = data_box[box_index]
        num = data_box_points
        if(box_index==0 or box_index %2==0):    #x축
            if(num > max_x):
                max_x = num
            if(num < min_x):
                min_x = num
        else:   #y축
            if(num > max_y):
                max_y = num
            if(num < min_y):
                min_y = num   
    bBox.append([max_x, max_y])
    bBox.append([min_x, min_y])
    print(bBox)
    json_object ={
        "label":classname,
        "points":bBox,
        "group_id":None,
        "shape_type":"rectangle",
        "flags":{}
    }
    return json_object
       
fileList = os.listdir('./')
try:
    os.mkdir(savePath)
except:
    print('폴더를 생성하지 않습니다')
json_list = []
for filename in fileList:
    if(filename.endswith('.json')):
        #json_list.append(os.path.join(path,filename))
        json_list.append(filename)

for jsonFile in json_list:
    print(jsonFile)
    result_dict = OrderedDict()
    result_dict['version'] = '5.0.1'
    result_dict['flags'] = {}
    result_dict['shapes'] = []
    with open(jsonFile, 'r', encoding='utf-8-sig') as r:
        data = json.load(r)
        filename = data['image']['filename']
        width = data['image']['resolution'][0]
        height = data['image']['resolution'][1]
        data_annotation = data["annotations"]
        data_annotation_len = len(data["annotations"])
        for index in range(data_annotation_len):
            if (data_annotation[index].get('polygon') is None):
                result = convCo2labelme(data_annotation[index])
            else:
                result = convCo2labelmePoly(data_annotation[index])
            result_dict['shapes'].append(result)
        result_dict['imagePath'] = filename
        result_dict['imageData'] = None
        result_dict['imageHeight'] = height
        result_dict['imageWeight'] = width
        with open(savePath+jsonFile,'w') as w:
            json.dump(result_dict,w,ensure_ascii=False,indent='\t')
            w.close()
