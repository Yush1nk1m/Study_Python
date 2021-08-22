# 모듈을 읽어 들입니다.
from urllib import request

# urlopen() 함수로 한빛출판네트워크의 이미지를 읽습니다.
target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb")
file.write(output)
file.close()