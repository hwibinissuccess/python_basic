# lambda 함수 = 익명함수(한번쓰고 버리겠다) : 한줄로 간단하게 함수를 정의하는 방법
# lambda args : expression

def add(x, y):
    return x+y

# 1. 람다 함수를 정의하고 사용
add = lambda x,y : x+y
res = add(2,3)
print(res)

# 2. 리스트 요소들을 제곱하는 람다함수, 'map()'함수로 사용
num = [1,2,3]
res2 = list(map(lambda x: x**2, num))
print(res2)

# 3. sorted(iterable, /, *, key=Node, reverse=False)를 활용해  dict를 가진 리스트를 특정키를 기준으로 정렬해보자
students = [{'name' : 'Aominica', 'age': 23},
            {'name' : 'Bominica', 'age': 21},
            {'name' : 'Cominica', 'age': 27}]

# 'age'키를 기준으로 정렬
res_sorted = sorted(students, key = lambda x : x['age'])
print(res_sorted)