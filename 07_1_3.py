# 모듈을 읽어 들입니다.
import os

# 폴더를 읽어 들이는 함수
def read_folder(path) :
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
    # 폴더의 요소 구분하기
    for item in output :
        if os.path.isdir(item) :
            read_folder(item)
        else :
            print('파일 :', item)

# 주소를 입력받고 해당 폴더의 파일/폴더를 전부 출력합니다.
link = input('주소 입력 >> ')
read_folder(link)