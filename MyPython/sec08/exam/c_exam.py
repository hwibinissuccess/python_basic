
# opener = None ) 사용자가 정의해서 오프너 지정(파일 경로와 플래그를 인수로 잡은 사용자 정의 함수 핸들링)
# 특수 파일 접근, 파일권한 설정, 로그 및 모니터링, 에러 또는 재시도 로직을 구현
import os
import datetime
import csv

### 1. 로그파일에 기록하는 함수
def log_access(action, path, mode):
    with open("file_access.log", 'a', encoding='utf-8') as logfile:
        logfile.write(f"{datetime.datetime.now()} - {action} : {path} (mode: {mode}) \n")
    with open("file_access.csv", 'a', newline='' ,encoding='utf-8') as csvfile:
        res = csvfile.writer(csvfile) # csv 파일을 생성시킴
        res.writerow([datetime.datetime.now(),action ,path, mode, mode]) # row 단위로 쓰겠다.

### 2. 사용자 오프너 함수
def my_openner(path, flags): #파일 경로와 플래그를 인수로 잡은 사용자 정의 함수
    # 로그 파일에 파일 읽기 기록
    log_access('OPEN', path, flags)
    return os.open(path, flags,mode=0o777) # 읽기권한(4) / 쓰기권한(2) / 실행권한(1)
    # mode 0o644 : 소유자는 읽기 및 쓰기, 그룹과 기타 사용자는 읽기만 하겠다.

### 3. 파일을 열때 사용자가 정의 오프너 사용해서 권한을 리턴 받는다.
with open('data03.txt', 'w', encoding='utf-8',opener=my_openner) as file:
    file.write("사용자 정의 함수 핸들링 \n")

### 4. 파일을 읽을 때 사용자가 정의 오프너 사용해서 권한을 리턴 받는다.
with open('data03.txt', 'r', encoding='utf-8',opener=my_openner) as file:
    res = file.read()
    print(res)

