import re
############ re 모듈의  주요 메소드 확인
def test01():
    pattern = r"hello"
    string = "hello world"
    match = re.match(pattern, string)

    if match:
        print("test01: 일치함")
    else:
        print("test01: 일치하지 않음")


def test02():
    pattern = r"world"
    string = "hello world"
    search = re.search(pattern, string) # 일치하는 첫번째 부분만 찾는다

    if search:
        print("test02: 일치함")
    else:
        print("test02: 일치하지 않음")


def test03():
    pattern = r"\d+"
    string = "There are 2 apples and 5 oranges"
    findall = re.findall(pattern, string)
    print(f"test03: {findall}")  # ['2', '5']


def test04():
    pattern = r"\d+"
    string = "There are 2 apples and 5 oranges"
    finditer = re.finditer(pattern, string)

    print("test04:")
    for match in finditer:
        print(match.group())  # 2, 5


def test05():
    pattern = r"apples"
    replacement = "bananas"
    string = "I like apples"
    new_string = re.sub(pattern, replacement, string)
    print(f"test05: {new_string}")  # "I like bananas"


def test06():
    pattern = r"\W+"
    string = "Words, words, words."
    split_list = re.split(pattern, string)
    print(f"test06: {split_list}")  # ['Words', 'words', 'words', '']


def test07():
    pattern = re.compile(r"\d+")
    string = "There are 2 apples and 5 oranges"
    findall = pattern.findall(string)
    print(f"test07: {findall}")  # ['2', '5']


def test08():
    pattern = r"\d{2}-\d{2}-\d{4}"
    string = "12-34-5678"
    fullmatch = re.fullmatch(pattern, string)

    if fullmatch:
        print("test08: 전체 문자열이 일치함")
    else:
        print("test08: 전체 문자열이 일치하지 않음")


def test09():
    string = "Hello. How are you?"
    escaped_string = re.escape(string)
    print(f"test09: {escaped_string}")  # Hello\. How are you\?


def test10():
    # 몇몇 정규 표현식 컴파일
    pattern1 = re.compile(r"\d+")
    pattern2 = re.compile(r"\w+")

    print(f"Cached patterns: {re._cache}")
    re.purge()
    print("test10: 캐시가 지워졌습니다.")
    print(f"Cached patterns: {re._cache}")


if __name__ == "__main__":
    while True:
        func_name = input("실행할 함수 이름을 입력하세요 (예: test01, 종료하려면 'exit' 입력): ")
        if func_name == "exit":
            break
        try:
            func = globals()[func_name]
            func()
        except KeyError:
            print(f"'{func_name}'은(는) 존재하지 않는 함수입니다. 다시 입력하세요.")