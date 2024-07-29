from functools import *


# 고차 함수 map(), filter(){, reduce()
# filter(function or Node, iteralbe) --> filter object
# -> 매개인자로 주어진 함수의 조건을 만족하는 요소들만을 리턴하는 함수
# 1. 짝수를 필터링 해보자
numbers = list(range(1,11))

# 짝수 필터링 함수
def is_even(n):
    return n%2==0

# filter() 적용
even_num = list(filter(is_even, numbers))
print(even_num)

# 2. 문자열 리스트 객체에서 특정 단어가 포함된 단어만 필터링하자
words =  ['사과', '바나나','수박', '복숭아'', 메론''딸기']

# '나'가 포함된 단어를 필터링 하는 함수
def contain_na(word):
    return '나' in word

na_str = list(filter(contain_na, words))
print(na_str)

# 리스트의 모든 요소를 더하자 reuce(function, iterable[,initial]) -> value
res = reduce(lambda x,y : x+y, [1,2,3,4,5])
print(res)

# 초기값도 줘보기
res = reduce(lambda x,y : x+y, [1,2,3,4,5], 100)
print(res)

ss = list(range(1,99))
res = reduce(lambda x,y: x*y,ss)
print(res)