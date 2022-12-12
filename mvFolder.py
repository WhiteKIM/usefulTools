import os
import shutil

PATH = os.path.abspath('./')
json_list = []#json파일명을 저장
json_path = []#json파일이 있는 위치와 파일명을 같이 저장
img_list = []#이미지파일명을 저장
img_path = []#이미지파일이 있는 위치와 파일명을 같이 저장

for (path, dir, files) in os.walk(PATH):
    for filename in files:
        fileroot = path+'\\'+filename
        if(filename.endswith('.json')):
            json_list.append(filename)
            json_path.append(fileroot)
        elif(filename.endswith('.jpg') or
        filename.endswith('.png') or
        filename.endswith('jpeg')):
            img_list.append(filename)
            img_path.append(fileroot)

for json, img, jsonRoot, imgRoot in zip(json_list, img_list, json_path, img_path):
    try:#이미 폴더가 존재한다면, 폴더를 생성하지 않고 이동을 수행, 없다면 폴더를 만듬
        os.mkdir(PATH+'\\'+'complete')
        shutil.move(jsonRoot, PATH+'\\'+'complete\\'+json)
        shutil.move(imgRoot, PATH+'\\'+'complete\\'+img)
    except:
        shutil.move(jsonRoot, PATH+'\\'+'complete\\'+json)
        shutil.move(imgRoot, PATH+'\\'+'complete\\'+img)
        continue