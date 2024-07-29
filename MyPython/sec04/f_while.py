def  test01():
    while False:
        print("abc")
    else:
        print('else')

def  test02():
    #1 + 2 +3 + 4 +  5
    su  = 1           #su  = 1
    while  su  <=  5:              # 1 <= 5(True)   /    2 <= 5(True)  / 3  <= 5 / 4 <= 5  / 5 <= 5 / 6 <= 5(False)
        print(su , end='\t')       # 1 2 3 4 5
        su = su + 1    # su = 2  su = 3 su= 4 su= 5 su= 6
    else:
        print(f' su  ={su }')

def  test03():
    # 1에서  5까지 합을 구해보자.    1 + 2
    su  = 1           #su  = 1
    sum = 0
    while  su  <=  5:              # 1 <= 5(True)   / 2 <= 5 (True)  /  3 <= 5 (True)   ....
        print(su , end='\t')       # 1  2   3
        sum = sum + su   #  sum  =  0 +  1  sum = 1 /  sum = 1+ 2  sum = 3 / sum = 3+ 3 sum= 6
        su = su + 1    #     su  = 2  su = 3 su = 4....
    else:
        print(f' sum  ={sum }')

def test04(): # 1~ 100까지 while  을 통해 출력 해보자.
    n=100
    cnt = 1
    while  cnt  <= n :
        print(f'{cnt}', end='\t')
        cnt = cnt+1

def test05(): # 1~ 100까지 while  을 통해 출력 해보자. 단  2의 배수만 출력 해보자.
    n=100
    cnt = 1
    while  cnt  <= n :
        if  cnt % 2 == 0:
            print(f'{cnt}', end='\t')
        cnt = cnt+1
def test06(): # 100 ~ 1 까지 출력 해 보자.
    n = 100
    cnt = 1
    while cnt <= n:
        print(f'{n}', end= '\t' )
        n = n - 1

if __name__ == '__main__':
    test06()





