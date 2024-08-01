import os

def f_test01():

    ### 파일을 a.txt로 생성해서 b.txt로 변경한 다음 삭제 해보기
    ### open() / os.rename() / os.remove()
    file_name = "a.txt"
    new_file = "b.txt"

    ### 1. 파일생성
    try:
        with open("a.txt", "w") as file:
            file.write("연습해보기!")
        print(f"{file_name} 파일생성 완료")
    except FileExistsError:
        print("이미 생성 완료")
    finally:
        print("~~~~~~~~~~~~~~~")

    ### 2. 파일이름 변경
    try:
        os.rename(file_name, new_file)
        print(f"파일 이름 {file_name}에서 {new_file}로 변경완료")
    except FileExistsError:
        print("이미 변경 완료")

    ### 3. 파일이름 삭제
    os.remove(new_file)
    print(f"파일 이름 {new_file} 삭제 완료")
def f_test02():
    ###  현재 작업 디렉토리에 있는 목록을 리턴 받아 출력하되 [디렉토리], [파일]로 표시해서 출력 해보기
    cur = os.chdir('c:/Users/user/Desktop')
    print(f"현재 작업 디렉토리 {cur}")
    print("=============list=================")
    directory = 'c:/Users/user/Desktop'
    for item in os.listdir('c:/Users/user/Desktop'):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item):
            print(f"[디렉토리] : {item}")
        elif os.path.isfile(item):
            print(f"[파일] : {item}" )
        else:
            print(f"넌 뭐야...? {item}")


def f_test03():
    ### 최상위 디렉토리를 받아서 하위 목록 출력 해보기
    for root, dirs, files in os.walk('c:/Users/user/Desktop'):
        for dir in dirs:
            print(f"[디렉토리] : {dir}")
            for file in files:
                print(f"[파일] : {file}")

def f_test04():
    from os.path import join, getsize

    cur = os.getcwd()
    for root, dirs, files in os.walk(cur):
        print(root, "consumes")
        print(sum(getsize(join(root, name)) for name in files), end =" ")
        print("bytes in", len(files), "non-directory files")

        if 'CVS' in dirs:
            dirs.remove('CVS')
            print("삭제완료")

def f_test05():
    ### 최상위 디렉토리를 받아서 하위 목록 출력 해보기
    directory = 'c:\\Users\\user\\Desktop'
    for root, dirs, files in os.walk(directory):
        lavel = root.replace(directory, '').count(os.sep) # 경로를 /를 cnt 한다
        indent = ' ' *4 * lavel
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' *4 * (lavel+1)
        for file in files:
            print(f"{sub_indent} {file}")

def f_test06(): # 특정 확장자 찾기
    directory = 'c:\\Users\\user\\Desktop'
    extension = "hwp"
    res = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                #res.append(os.path.join(root, file))
                print(os.path.join(root,file))
    #print(len(res), res)




if __name__ == '__main__':
    f_test06()