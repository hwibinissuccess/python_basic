def test01():
    #range(start,stop-1,step size)
    range(10)
    r=list(range(10))
    r1= list(range(2,8))
    r2= list(range(2,20,3))
    for  x  in r :
        print (x , end ='\t')

    for x  in r1:
        print (x, end ='\t')

    for  x in r2 :
        print(x, end ='\t')

def test02():
    #r,r1,r2가 가진 세가지 범위를 리스트 객체로 생성하고, my_r[]
    # 각 리스트를 반복하면서  for
    # 요소를 문자열로 변환하고  map(str,my_r)  : 고차함수
    # 탭으로 구분해서 출력 하자.  '\t'.join()

    #############1.  세가지 범위를 리스트 객체로 생성하고, my_r[]
    my_r=[list(range(10)) ,
          list(range(2,8)),
          list(range(2,20,3))
          ]
    ##############2. 각 리스트를 반복하면서  for
    for  r  in my_r:
        # 3. 요소를 문자열로 변환하고  map(str,my_r)  : 고차함수
        # 탭으로 구분해서 출력 하자.  '\t'.join()
        print('\t'.join(map(str, r)))

if __name__ == '__main__':
    test02()

