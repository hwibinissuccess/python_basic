# 파일의 임의 접근을 해보자
# seek(offset(파일포인터를 이동시킬 바이트 수),
#       whence(기존 위치 지정 0,1,2))
# 'SEEK_SET'(0) : 파일시작 기준으로 이동
# 'SEEK_CUR'(1) : 현재 파일 포인터 기준으로 이동
# 'SEEK_END'(2) : 파일의 끝을 기준으로 이동


def Test01():
    with open("res/test", "rb") as file: # rb => byte로 바꿔준 것 b안 들어가면 오류남, 바이너리 타입으로 바꿔준 것
        # 파일의 처음에서 5개 이동
        file.seek(5,0)
        print(file.read(10), "curr:", file.tell()) # 옮긴 위치에서 10byte

        # 현재 위치에서 10개 앞으로 이동, 10byte 출력
        file.seek(10, 2)
        print(file.read(10),"curr:", file.tell())

        # 파일의 끝을 기준으로 10개 이동, 10byte출력
        file.seek(-10, 2)
        print(file.read(10), "curr:", file.tell())

def Test02(): # with문 사용하지 않음
    f = open("res/test", "r")
    f.seek(1)  # 파일포인트를 특정 위치로
    print(f.tell())  # 현재 위치 리턴
    print(f.read(1))
    print(f.tell())
    f.close()
    print(type(f))

if __name__ == '__main__':
    Test01()

