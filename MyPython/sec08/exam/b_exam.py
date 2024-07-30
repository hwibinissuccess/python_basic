
# opener = None ) 사용자가 정의해서 오프너 지정(파일 경로와 플래그를 인수로 잡은 사용자 정의 함수 핸들링)
# 특수 파일 접근, 파일권한 설정, 로그 및 모니터링, 에러 또는 재시도 로직을 구현
import os

def my_openner(path, flags): #파일 경로와 플래그를 인수로 잡은 사용자 정의 함수
    return os.open(path, flags,mode=0o777) # 읽기권한(4) / 쓰기권한(2) / 실행권한(1)
    # mode 0o644 : 소유자는 읽기 및 쓰기, 그룹과 기타 사용자는 읽기만 하겠다.

with open('data03.txt', 'w', encoding='utf-8',opener=my_openner) as file:
    file.write("사용자 정의 함수 핸들링")


f = open('data03.txt', 'w', encoding='utf-8',opener=my_openner) # 내장 open 함수ㅋ
print(type(f))