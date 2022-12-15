# usefulTools
라벨링 작업에서 사용하기 위해 만들었던 도구입니다.

## Introduce
1. coco2labelme : coco형식으로 만들어진 json을 labelme형식의 json으로 변환
2. Findoverlap : 중복으로 사용되지 않는 객체를 중복으로 잡은 경우에 이를 제거
3. img2video : 이미지파일을 이용하여 동영상파일로 만들때 사용
4. labelme2yolo : labelme형식의 json을 yolo에서 사용하는 txt파일로 변환 ※ yolov5
5. labelme2yolo_noImg : 4번과 동일하나 images폴더로 이미지 파일로 옮겨주는 작업 제거 ※ yolov5
6. makeFolder : 2000개의 파일을 폴더를 만들어 각각 나누어 이동
7. makeJson : labelme에서 동일한 위치에 동일한 객체가 잡혀있는 json의 경우, 작업을 줄이고 시간을 절약하기 위해 사용
8. makeJson_upgrade : 7번에서 파일명이 잘 정리되지 않아 이를 해결함
9. misPrintFix : label의 이름을 잘못지정한 경우에 이를 일괄적으로 변경할 수 있음
10. mvFolder : json파일과 이미지 파일을 일괄로 이동
11. rm_empJsonAndIMG : labelme의 경우 ctrl+p 기능을 통해 이전 json정보를 다음 이미지 파일에 적용할 수 있는데, 이 경우 객체가 없어 모든 폴리곤을 제거하여도 json이 남는 경우가 발생하여, 이렇게 아무런 정보가 없는 json을 제거하는 기능
12. test_yolo_annotation : 변환된 yolo용 라벨이 잘 잡혀있는지 확인할 수 있음
13. labelme2yolov7 : 업로드 예정
