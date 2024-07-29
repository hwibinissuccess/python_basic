from functools import *

 #(팩토리얼 계산, 피보나치 수열 ), 하노이탑
def factorial(n):
    print(f'---------{n}')
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#피보나치 수열  : 이전 두 숫자의 합이 현재 숫자가 되는 수열
#수열 :  일반항, 유한,무한, 수열의 종류 (나열된 원소의 정렬) , 등차수열, 등비수열, 피보나치 수열
#수열: 숫자나 기호의 나열이며 일정한 규칙이나 패턴에 따라 정렬되어 있는 것
def fibonacci(n):
    if n <=0  :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

def fibonacci02(n):
    # 수열을 생성하는 초기 값
    init = (0, 1)
    def my_view(prev, _):
        res = (prev[1], prev[0] + prev[1])
        print(f"reduce({prev}) = {res}")
        return res

    # 피보나치 수열 생성
    f_res = reduce(my_view, range(n - 1), init)
    return f_res[1]

if __name__ == '__main__':
    #print(factorial(5))
    res =  fibonacci(10)
    print("피보나이츠 수열의 10번째 값  :" , res)

    # 피보나치 수열의 첫 10개의 항을 생성
    n_terms = 3
    f = [fibonacci02(n) for n in range(1, n_terms + 1)]
    print(f)


