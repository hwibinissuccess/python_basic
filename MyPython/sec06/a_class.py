from sec06.exam.Mycalc import Calc

if __name__ == '__main__':
    c1  = Calc() ;    c2  = Calc(100);     c3=   Calc(3,4)
    print(c1.__str__() )
    print(c2.__str__())
    print(c3.__str__())
    print('====================1. 클래스의 목록 확인  dir()==================================')
    print(dir(c1))
    print('====================2. 인덱스 명시 호출       ==================================')
    test_all  =  [Calc (100,200) , Calc(10,5) , Calc(10,2)]
    print ( test_all[0], test_all[1] , test_all[2] )
    print(test_all[1].getHap())
    print(test_all[2].getSub())
    for  res  in test_all: ##전체 반복 출력
        print(res )  #res.__str__()

    print('====================3. 리스트 언팩킹 : 나열형 값(시퀀스)을 여러변수에 할당=================')
    test_all02 = [Calc(100, 200), Calc(10, 5), Calc(10, 2)]
    print( *test_all02)

    print('====================4. 람다식  =================')
    test_all03 = [Calc(100, 200), Calc(15, 5), Calc(8,2)]
    list(  map(lambda  res : print(res)  , test_all03  ) )

















