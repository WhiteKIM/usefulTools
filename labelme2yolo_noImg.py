import json
import os
import shutil

default_label_path = './labels' # Yolo를 위한 라벨이 저장될 폴더
default_img_path = './images'   # Yolo를 위한 이미지가 저장될 폴더

class_name = []

# labelme 좌표를 Yolo형식의 좌표값으로 변경하는 함수
# 인자값 : labelme형식의 json파일
# 반환값 : X
def convlabelMe2Yolo(jsonFile):
    with open(jsonFile,'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        dw = 1./data["imageWidth"]
        dh = 1./data["imageHeight"]
        box = data['shapes']
        for box_data in range(len(box)):    # 이미지 내에 객체가 두 개 이상일 경우를 반영
            box_data_data = box[box_data]['points']
            if(box[box_data]['label'] not in class_name):
                class_name.append(box[box_data]['label'])
            min_x = 10000000
            min_y = 10000000
            max_x = 0
            max_y = 0
            for box_point in range(len(box_data_data)):
                box_point_data = box_data_data[box_point]
                for box_point_index in range(len(box_point_data)):
                    num = box_point_data[box_point_index]
                    if(box_point_index==0 or box_point_index%2==0):
                        # x축 좌표
                        if(num > max_x):
                            max_x = num
                        if(num < min_x):
                            min_x = num
                    else:# y축 좌표
                        if(num > max_y):
                            max_y = num
                        if(num < min_y):
                            min_y = num
                          
            x=(max_x+min_x)/2.0
            y=(max_y+min_y)/2.0
            w=max_x - min_x
            h=max_y -min_y
            x = x*dw
            w = w*dw
            y = y*dh
            h = h*dh
            with open(default_label_path+'/'+os.path.splitext(jsonFile)[0]+'.txt', 'a') as txtfile:
                txtfile.write(str(class_name.index(box[box_data]['label']))+' '+str(x)+' '+str(y)+' '+str(w)+' '+str(y)+'\n')
                txtfile.close()
        
#소스파일이 위치한 곳에서 작업을 수행
fileList = os.listdir('./')
image_List = []
json_List = []
#폴더가 존재할 경우를 대비
try:
    os.mkdir(default_img_path)
except:
    print('img 폴더 존재')

try:
    os.mkdir(default_label_path)
except:
    print('txt폴더 존재')

for fileName in fileList:
    if(fileName.endswith('.png') or 
    fileName.endswith('jpg') or
    fileName.endswith('jpeg')):
        image_List.append(fileName)
    elif(fileName.endswith('.json')):
        json_List.append(fileName)

for fileName in json_List:
    convlabelMe2Yolo(fileName)

for fileName in image_List:
    shutil.copy(fileName, default_img_path+'/'+fileName)    #images 폴더에 사진 복사