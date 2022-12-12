# 오탈자 찾아서 변경
import json
import os

print('오탈자 찾기')

fileList = os.listdir('./')
jsonList = []
label_class =[] 

for filename in fileList:
    if(filename.endswith('.json')):
        jsonList.append(filename)

for jsonFile in jsonList:
    with open(jsonFile, 'r') as f:
        data = json.load(f)
        for i in range(len(data['shapes'])):
            label = data['shapes'][i]['label']
            if(label not in label_class):
                label_class.append(data['shapes'][i]['label'])
        f.close()

print('찾아낸 모든 라벨 이름')
print(label_class)
print('변경하고 싶은 라벨 이름 입력 : ', end=' ')
before = input()
print('변경될 라벨 이름 입력 : ', end=' ')
after = input()

for jsonFile in jsonList:
    check = False
    with open(jsonFile, 'r+') as f:
        data = json.load(f)
        for i in range(len(data['shapes'])):
            if(data['shapes'][i]['label']==before):
                data['shapes'][i]['label'] = after
                check = True
        f.seek(0)
        json.dump(data, f, ensure_ascii=False, indent='\t')
        f.close()