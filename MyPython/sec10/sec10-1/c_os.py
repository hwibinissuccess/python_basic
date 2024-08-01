import glob
import os


def test01():
    #현재 디렉토리에 있는 .py확장자를 가진 파일을 찾기
    #  * (o,more)   + (1,more)  ?(1개문자)  [a-z] 대괄호안에 있는 문자를 매치 ,  ** 모든디렉토리
    res =glob.glob('**/*.py', recursive=True)
    print(res)

def test02():
    #검색할 디렉토리 경로
    dir  = r'C:\Mywork\MyPython'  # raw string
    print(dir)
    res =glob.glob(os.path.join(dir,'**','*.py' ), recursive=True)

    #출력
    for file in res:
        print(os.path.basename(file))


if __name__ == '__main__':
    test02()