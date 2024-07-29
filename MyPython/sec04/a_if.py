#단일 if 연습
def case01():
    #만일에  True이면 "abcde", 1,2,2를 출력해 보자.
    if True:
        print("abcd")
        print(1)
        print(2)
        print(2)
def case02(): # 만일에 True이면 True를 리턴하자.
    if True:
        return True

def case03() : #만일에 False이면 False를 리턴하자.
    fw = False
    if fw == False:  # 조건의 결과를 True로 만들어 준다.
        return False

def case04(): #return 없는 함수
    pass

if __name__ == '__main__':
    res= case04()  # 아무것도 return  안했어
    print(res)   # 받아서 출력할 것이 없어 None
    res = case03()
    print(res)