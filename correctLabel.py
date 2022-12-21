import json
import os

FileList = os.listdir('./')#현재 위치한 폴더
JsonList = []

for file in FileList:
    if(file.endswith('.json')):
        JsonList.append(file)

target_Index = 0
print("Input Index: " , end='')
target_Index = int(input())#입력한 값의 인덱스 json을 기준으로 잘못된 json수정
target_Json = JsonList[target_Index]

for JsonIndex in range(target_Index+1 ,len(JsonList)):
    with open(target_Json, 'r') as f1:
        data1 = json.load(f1)
        with open(JsonList[JsonIndex], 'r') as f2:
            data2 = json.load(f2)
            with open(JsonList[JsonIndex], 'w') as f3:
                for i in range(len(data1['shapes'])):
                    data2['shapes'][i] = data1['shapes'][i]
                json.dump(data2, f3, ensure_ascii=False, indent='\t')
                f3.close()
            f2.close()
        f1.close()