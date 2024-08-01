import os

def test01():
    #1. c:\Test02 폴더를 만들자
    dir_name ="c:\\test02"
    try:
        os.mkdir(dir_name)
        print(f'{dir_name} 은 생성되었다.' )
    except FileExistsError:
        print(f'{dir_name } 은 이미 존재 한다')

def test02():
    #2. c:/Test03/a/b/c/d  폴더를 만들자   중첩 디렉토리 생성
    dir_name ="c:/Test03/a/b/c/d"
    try:
        os.makedirs(dir_name)
        print(f'{dir_name} 은 생성되었다.' )
    except FileExistsError:
        print(f'{dir_name } 은 이미 존재 한다')

def test03():
    #3. c:/Test03/a/b/c/d  폴더를 만들자   중첩 디렉토리 생성
    dir_name ="c:/Test03/a/b/c/d"
    os.makedirs(dir_name,exist_ok=True)
    print(f'{dir_name } 은 새로 생성했다 ')

if __name__ == '__main__':
    test03()