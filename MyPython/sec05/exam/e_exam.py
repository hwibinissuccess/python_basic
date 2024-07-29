from  functools import reduce

def my(x):
    return x*2
def Test01_map():
    numbers  = [1,2,3,4,5]
    res = map(my,numbers)
    print(list(res))
def my02(x):
     if  x % 2 == 0 :
        print(x)
        return x
def Test02_filter():
    numbers = [1, 2, 3, 4, 5]
    #res = filter(lambda x: x % 2 ==0, numbers)
    res = filter(my02, numbers)
    print(list(res))

def Test03_reduce():
    numbers = [1, 2, 3, 4, 5]
    res = reduce(lambda x,y : x * y, numbers)  #((((1*2)*3)*4)*5).
    print(res)

def Test04_filter(): # 1~100까지 홀수만 필터해서 출력

    num = range(1,101)
    res = list(filter(lambda x : x%2 == 1, num))
    print(res)

def Test05_exam():
    # 1~20까지의 리스트 객체를 제곱하고 / 100보다 큰 값을 필터링 한 다음 / 이 값을 모두 더하자
    # 데이터 변환 -> 필터링 -> 집계

    num = list(map(lambda x : x**2, range(1,21)))
    fil = list(filter(lambda x : x>100, num))
    res = int(reduce(lambda x,y : x+y, fil))
    print(res)

def Test06_exam():
    # 1~20까지의 리스트 객체를 제곱하고 / 100보다 큰 값을 필터링 한 다음 / 이 값을 모두 더하자
    # 데이터 변환 -> 필터링 -> 집계

    num = list(map(lambda x : x**2, range(1,21)))
    fil = list(filter(lambda x : x>100, num))
    res = reduce(lambda x,y : x+y, fil)
    print(f'map : {num}')
    print(f'fil : {fil}')
    print(f'reduce : {res}')

def Test07_exam(): # 1~20까지의 리스트 객체의 요소 중 홀수를 두배로 만들고 20보다 큰 값을 필터링 한 후, 값을 모두 더하자 # 집계 결과만 확인
    res = reduce(lambda x,y : x+y, list(filter(lambda x : x>20, list(map(lambda x : x*2 if x%2 == 1 else x, range(1,21))))))
    print(res)

if __name__ == '__main__':
     Test01_map()
     Test02_filter()
     Test03_reduce()
     Test04_filter()
     Test05_exam()
     Test06_exam()
     Test07_exam()
