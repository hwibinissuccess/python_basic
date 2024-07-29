from functools import singledispatch   # 함수의 오버로딩을 만드는데 사용하는 것

'''
같은 함수이름을 매개인자 또는 데이터타입을 다르게 지정해서 호출하는 기능
1. 임의 함수 위에 @singledispatch 지정
2. @함수명.register 라는 데코레이터를 오버로드 함수에 위에 선언
'''
@singledispatch
def  my_data(data) :
    print("Error")

# tuple를 받아서 출력하는 my_data 함수를 오버로드 하고 싶다.
@my_data.register
def _(res : tuple):
    print('tuple 전용 공간 :', res)

@my_data.register
def _(data :int, t :int):
    print(" int  " , data , t)
@my_data.register
def _(data :str):
    print(" str  " , data)
@my_data.register
def _(data:list):
    print("list" , data)

if __name__ == '__main__':
      my_data(10 ,100)
      my_data("abc")
      my_data([1,2,3,])
      my_data(90.9)
      my_data((1,2,3))