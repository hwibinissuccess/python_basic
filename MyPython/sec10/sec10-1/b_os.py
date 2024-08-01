import os

def f_test01():
    #########  파일을 a.txt로 생성해서  b.txt로 변경 한 다음 삭제 해보자
    ###########  open()  /  os.rename() / os.remove()
    file_name ="a.txt"
    new_file  ="b.txt"

    ###1. 파일생성
    try:
        with  open("a.txt","w") as file:
            file.write("연습용!!!")
        print(f'파일생성했어  {file_name }')
    except FileExistsError:
        print(" 이미 생성되었어  ")
    finally:
        print("~~~~~~~~~~~~~~~~~")

    ###2. 파일이름 변경
    try:
        os.rename(file_name, new_file)
        print(f'파일 이름이  {file_name}에서  {new_file}로 변경됨  ')
    except FileExistsError:
        print(" 이미 변경되었어 ")

    ###3. 파일이름 삭제
    os.remove(new_file)
    print(f'파일 이름 {new_file} 이 삭제 되었어 ')




def f_test02():
    ######### 현재 작업디렉토리에 있는 목록을 리턴 받아 출력하되 [디렉토리 ] , [파일] 로 표시해서 출력 해보자.
    cur   = os.getcwd()
    print(f'현재 작업 디렉토리  {cur}')
    print('==================== list  =============')
    directory  = 'c:\\Windows'
    for item in  os.listdir(directory):
        item_path  = os.path.join(directory,item)
        if os.path.isdir(item_path):
            print(f'[디렉토리] : { item}')
        elif os.path.isfile(item_path):
            print(f'[파일]  :   { item}')
        else:
            print(f'넌 뭘까? :  { item}')

        #print(item_path)


def f_test03():
    ###### 최상위 디렉토리를  트리로  하위 목록 출력 해보자.
    for root, dirs, files in os.walk('C://Mywork//MyPython'):
        for  dir  in dirs:
            print(f'[디렉토리] : { dir}')
        for  file in files:
            print(f'[파일]  :   {file}')


def f_test04():
    import os
    from os.path import join, getsize

    cur = os.getcwd()
    for root, dirs, files in os.walk(cur):
        print(root, "consumes ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories
            print("삭제 했어 ")

def f_test05():
    ###### 최상위 디렉토리를  트리로  하위 목록 출력 해보자.
    directory  ='C:\\Mywork\\MyPython'
    for root, dirs, files in os.walk(directory):
        #print(type(root.replace(directory,'')))
        level  = root.replace(directory,'').count(os.sep)  #경로를 /를 cnt 한다
        indent  = ' ' *4 * level
        print(f'{indent}{os.path.basename(root)}/')
        sub_indent= ' ' *4 * (level+1)
        for file in files:
            print(f'{sub_indent}{file}')
def f_test06():# 특정 확장자 찾기  py찾자
    directory = 'C:\\Mywork\\MyPython'
    extension  ="py"
    res  = []
    for root, dirs, files in os.walk(directory):
        for file in files:
             if file.endswith(extension):
                 res.append(os.path.join(root, file))

    print(len(res) , res)


if __name__ == '__main__':
    f_test06()
