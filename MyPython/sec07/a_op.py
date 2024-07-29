
class MyClass:
    def __init__(self ,value):
        self.value = value

    def __add__(self, other):
        print("__add__")
        return self.value + other.value

    def __radd__(self, other): # 오른쪽 피연산자(other)와 현재 객체를 더한 값을 반환
        print("__radd__")
        return other.value + self.value # add와 비교했을때 위치바꿈

    def __ge__(self, other): # 재정의 / 크거나 같다
        print("__ge__")
        return self.value >= other.value

    def __gt__(self, other): # 재정의 / 크다
        print("__gt__")
        return self.value > other.value

    def __eq__(self, other): # 재정의 / 같다
        print("__eq__")
        return self.value > other.value

if __name__ == '__main__':
    obj = MyClass(5)
    obj01 = MyClass(10)
    hap = obj+obj01
    print(hap)
    '''
    print(obj, obj01)
    print(f'hap = {hap}')
    res = obj > obj01
    print(res)
    '''

