import re
def test01():
    p = re.compile('ab*')
    print(p, type(p)) #<class 're,Pattern'>

    p = re.compile(r"\d+") # 10진 숫자 1 more , \w = 알파벳 문자, 숫자, _ , \s = 공백문자(스페이스, 탭, 엔터), \ = 메타
    print(p, type(p))  # <class 're,Pattern'>
    p = re.compile(r"\w")
    p = re.compile(r"\s")
    p = re.compile(r".") # 임의의 한문자와 일치
    target = "C:\PythonWork\myenv\Scripts\python.exe add C:\PythonWork\python_basic\MyPython\sec10\sec10-3\a_re.py" # str
    res_all = p.findall(target) # 정규객체.findall(대상)
    res_all = re.findall(r".",target) # re.findall(패턴, 대상)
    print(res_all)

def test02():
    target = "C:\PythonWork\myenv\Scripts\python.exe add C:\PythonWork\python_basic\MyPython\sec10\sec10-3\a_re.py" # str
    target = ["ab", "aB", "AAABBB", "a", "b", "dddAB"]
    # ab* 정규화 표현식을 표현하되, 대소문자는 무시하겠다. = 대소문자 구분하지 않고 문자열을 설정
    p = re.compile('ab*', re.IGNORECASE)
    # 문자열에서 패턴을 찾아보기
    for res in target:
        match_res = p.match(res)
        if match_res:
            print(f"{res} matches the pattern '{p.pattern}'")
        else:
            print(f"{res} does not catchs the paatern {p.pattern}")

def test03():
    target = ["a\nb", "A\nB", " A.b", "a b"]
    # 여러 플래그를 사용해보자
    # ^a : a로 시작하고 / a.b : a 다음에 임의의 한 문자가 오고 b가 오고 / b$ : b로 끝나는 문자열
    p = re.compile(r'^a.b$', re.I | re.DOTALL | re.VERBOSE) # re.M(멀티라인 약자) 시작(^) 끝($)을 각 줄의 시작과 끝으로 인식한다. / re.s
                                                                   # re.VERBOSE = 공백, 주석포함 / re.Dotall : 줄바꿈 문자열 제외 다 가져옴
    # 문자열에서 패턴을 찾아보기
    for res in target:
        match_res = p.match(res)
        if match_res:
            print(f"{res} matches the pattern '{p.pattern}'")
        else:
            print(f"{res} does not catchs the paatern {p.pattern}")

def test04():
    # 이메일 패턴 구현
    email_p = r"[a-zA-z0-9._]+@[a-zA-Z0-9]+\.[a-zA-z]{2,}$"
    tel_p = r"^\d{2,3}-\d{3,4}-\d{4}$"
    string = " 010 -1234-5678"
    res = re.match(tel_p, string)

    if res:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    test03()