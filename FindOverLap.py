#fire, smoke는 중복으로 존재 X
# 이것을 중복으로 존재하는 json파일을 알려줌

import json
import os

# overlap 구조 0번째 -> fire, 1번째 smoke, 2번째 person
overlap = []
jsonList = []
fileList = os.listdir('./')

for filename in fileList:
    if(filename.endswith('.json')):
        jsonList.append(filename)

temp = sorted(jsonList,key=lambda json_num: int(os.path.splitext(json_num)[0]))
jsonList= temp

for file in jsonList:
    with open(file, 'r') as f:
        data = json.load(f)
        fire_cnt = 0
        smoek_cnt = 0
        person_cnt = 0
        for i in range(len(data['shapes'])):
            label = data['shapes'][i]['label']
            if(label == 'fire'):
                fire_cnt+=1
            elif(label == 'smoke'):
                smoek_cnt+=1
            elif(label=='person'):
                person_cnt +=1
        overlap.append([fire_cnt, smoek_cnt, person_cnt])
        f.close()

print('중복 검색')

index = 0
for lap in overlap:
    if(lap[0]>1 or lap[1]>1):
        print('라벨 중복 파일 :'+jsonList[index])
    index+=1