#객체간의 연산[ 산술, 관계, 비교]  ->  사용자  객체정렬을  구현하는 재정의 메소드
#https://docs.python.org/3.12/reference/datamodel.html#object.__gt__
class MyClass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):  #재정의
        print("__add __")
        return self.value + other.value

    def __radd__(self, other):  # 오른쪽 피연산자(other) 와  현재 객체를 더한 값을 반환
        print("__radd __")
        return other.value +self.value

    def __ge__(self, other):  # 재정의
        print(" __ge__")
        return self.value >= other.value

    def __gt__(self, other):  # 재정의
        print(" __gt__")
        return self.value > other.value

    def __eq__(self, other):  # 재정의
        print(" __eq__")
        return self.value  ==  other.value



if __name__ == '__main__':

    obj   = MyClass(5)  # 숫자 하나 관리하는 클래스
    obj01  = MyClass(10)
    hap  = obj+ obj01
    print(hap)
    '''
    print(obj, obj01)
    #hap  = obj01 + obj # 10 +  5  = 15
    #print(f'hap = {hap}' )
    res  =   obj  >=  obj01
    print(res)
    res  = obj  > obj01
    print(res)
    '''

