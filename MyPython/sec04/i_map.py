# map(func, *iterables) --> map object   : 고차 함수

num  =[1,2,3,4,5]
#각 제곱을 구현하는 함수
def square(x):
    return  x * x

def case01():
    #1. 리스트의 각요소를 제곱하는 예제를 만들자
    res   = list(map(square, num))
    print(res)

def case02():
    #2.문자열로 구성된 리스트를 정수로 변환해 보자.
    data  =  ['1' ,'2','3','4','5']
    res  =  list(map(int, data))
    print(res)

def case03():
    #3.문자열의 길이를 계산해보자.
    data  =  ["홍길동","abcdefg" ,"서울시 강남구 도곡동" ,  "제주도"]
    length  = list(map(len,data)) # len(obj)
    print(length)

def case04():
    #4.각 자료를 대문자로 변환하자.   str.upper() , map을 사용하자.
    fruit = ['apple', 'watermelon', 'peach', 'pear']
    res  = list(map(str.upper, fruit))
    print(res)

if __name__ == '__main__':
    case04()
    ## 고차함수중 map(함수, 반복가능객체 )는 함수가 적용된 결과를 반환하는 함수 = 반복문 대처