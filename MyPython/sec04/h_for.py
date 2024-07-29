def test01():
    #1~ 4 리스트 객체를 출력 해보자.
    for  res  in  [1,2,3,4]:
        print(f'{res}',end ='\t')

def test02():
    #1~ 4 tuple 객체를 출력 해보자.
    for res in (1,2,3,4):
        print(f'{res}' ,  end='\t')

def test03():
    #print(range(10), list(range(10)) , list(range(0,101,2)))
    for  res  in range(0,101,2):
        print(f'{res}' , end ='\t')

def test04():
    #0 ~ 100까지 정수를 출력하되 5의 배수만 출력하고 싶다. range(), for()
    for res in range(0,101,5):
        print(f'{res}' , end ='\t')
    print(f'\n{"-" *100}')  # 속도 빠름 / 가독성 좋음  ver. 3.6권장
    # https://docs.python.org/3/whatsnew/3.12.html  f' 멀티라인 과 중첩 f-string

    res  = list(range(100, -1, -5))
    for   x in res:
        print(f'{x}' , end='\t')

def test05():
    fruit  =  ['apple' , 'watermelon' , 'peach' ,'pear']
    for  res  in  fruit:
        for  x  in res:
            print(x  ,end='\t')
        print()

def test06():
    #문자열을  거꾸로 뒤집어서 출력하고 싶다.  fruit[::-1]
    fruit  =  ['apple' , 'watermelon' , 'peach' ,'pear']
    print( f'{fruit[::-1]}') # 재확인
    x= fruit[0]
    print( f'{x [::-1]}')

    print(f'\n{"-" * 100}')
    for res  in fruit:
        r_res  = res[::-1]
        print(f'{r_res}')

def test07():
    # fruit의 글자 수가 5개 이상인 글자만 출력 해보자
    fruit = ['apple', 'watermelon', 'peach', 'pear']
    print(len(fruit))
    for res in fruit:
        if len(res)   >  5:
            print(res, len(res))


if __name__ == '__main__':
    test07()