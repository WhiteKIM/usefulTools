import datetime
import os
import json
import time

json_file = []
ext_json_file = []
img_file = []
img_count = 0
json_count = 0
PATH = os.path.dirname(os.path.abspath(__file__))
rootpath = os.path.join(PATH, 'trespass')
start = time.time()

for (path, dir, files) in os.walk(rootpath):  
    for filename in files:
        if(filename.endswith('.png')):
            img_file.append(os.path.join(path,os.path.splitext(filename)[0]))
        elif(filename.endswith('.json')):
            ext_json_file.append(os.path.join(path,os.path.splitext(filename)[0]))
            json_file.append(os.path.join(path,filename))

for img in img_file:
    if img not in ext_json_file:
        os.remove(img+'.png')
        img_count+=1

for file in json_file:
    with open(file, 'r') as f:
        data = json.load(f)
        json_shape = data['shapes']
        f.close()
        if(len(json_shape)==0):
            os.remove(file)
            json_count+=1

img_file.clear()
json_file.clear()
ext_json_file.clear()
for (path, dir, files) in os.walk(rootpath):  
    for filename in files:
        if(filename.endswith('.png')):
            img_file.append(os.path.join(path,os.path.splitext(filename)[0]))
        elif(filename.endswith('.json')):
            ext_json_file.append(os.path.join(path,os.path.splitext(filename)[0]))
            json_file.append(os.path.join(path,filename))

for img in img_file:
    if img not in ext_json_file:
        os.remove(img+'.png')
        img_count+=1

end = time.time()-start
times= str(datetime.timedelta(seconds=end)).split(".")
times = times[0]
print('경과 시간: '+times)
print('제거된 이미지 파일 개수 :'+str(img_count))
print('제거된 JSON 파일 개수 :'+str(json_count))
