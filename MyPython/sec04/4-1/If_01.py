def  If_test():
    #1. 입력받은 문자열 id가 "a1234"이면 출력하자.
    my_id= input("Enter your id: ")
    if my_id == "a1234":  # 값 비교
        print("true :", my_id)

def  If_test02():   #  >   <    >=  <=   ==   !=  ->bool
    ##  2. 입력 받은 my_id가  "a1234"와 같지 않다면 출력하자.
    my_id= input("Enter your id: ")
    if my_id != "a1234":  #  입력 받은 my_id가  "a1234"와 같지 않다면
        print("true :", my_id)

def If_test03():
    #3. 조건이 None이면 True 출력, False 면 'False'출력, 그외 'etc'출력하자.
    if None:
        print("True")
    elif False:
        print("False")
    else:
        print("etc...")

if __name__ == '__main__':
  If_test03()