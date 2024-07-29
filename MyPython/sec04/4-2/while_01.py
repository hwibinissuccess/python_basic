def w_test01():
    # 1~ 10까지 정수를 출력하고 합을 출력하자.
    i = 1
    sum =0
    while  i <= 10: # 1 <=10, 2<=10, 3<=10,,,, 10<= 10 , 11 <=10 -False
        print(i)    #  1  2   3  ,,,,, 10
        sum += i
        i   += 1      #  2  3   4....    11
    else:
        print(f'====> {i} :   {sum}')  #false 영역

def w_test02(start, end ):
    # 1~ 10까지 정수를 출력하고 합을 출력하자.
    i = start
    sum =0
    while  i <= end: # 1 <=10, 2<=10, 3<=10,,,, 10<= 10 , 11 <=10 -False
        print(i)    #  1  2   3  ,,,,, 10
        sum += i
        i   += 1      #  2  3   4....    11
    else:
        #print(f'====> {i} :   {sum}')  #false 영역
        return sum

print(" G영역  ")
if __name__ == '__main__':
    w_test01()
    print("  start, end 값을 입력해서 합을 리턴을 받는 w_test02()를  구현하자. ")
    hap  = w_test02(1, 10 )
    print(f'hap  = {hap}')
