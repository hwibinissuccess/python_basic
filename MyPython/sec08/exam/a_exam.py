

def test01(file_name):
    # 텍스트 파일 읽기
    with open(file_name,'r') as file: # () 안에 있는 속성을 file이라는 별칭으로 선언
        res = file.read()
        print(res)

def test02():
    # 텍스트 파일 쓰기
    with open('data02.txt','w') as f: #()안에 속성을 가진 f라는 별칭
        f.write("최휘빈은 2024 하반기 취뽀한다!\n")
        f.write("대기업, 금융권에!!!")

def test03():
    # 텍스트 파일 추가하기 쓰기
    with open('data02.txt','a') as f: #()안에 속성을 가진 f라는 별칭
        f.write("최휘빈은 2024 하반기 취뽀한다!\n")
        f.write("대기업, 금융권에!!!")

if __name__ == '__main__':
    file_name = 'data02.txt'
    test01(file_name)