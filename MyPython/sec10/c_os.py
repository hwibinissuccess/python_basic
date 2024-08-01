import glob
import os

def tset01():
    # 현재 디렉토리에 있는 ()안에 있는 확장자를 가진 파일을 모두 찾는다
    # * (o, more) + (1, more) ? (1개문자) [a-z] 대괄호안에 있는 문자를 매치, ** 모든 디렉토리
    res = glob.glob('**/*.py', recursive=True)
    print(res)

def test02():
    # 검색할 디렉토리 경로
    dir = r'/'  # r = raw String의 약자
    print(dir)
    res = glob.glob(os.path.join(dir, '**','*.py'), recursive=True)

    # 출력
    for file in res:
        print(file)

if __name__ == '__main__':
    test02()