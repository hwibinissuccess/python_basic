# 객체의 문자열 표현 __str__() / __repr__() 재정의
class MyClass :

    def __init__(self, val):
        self.val = val # 객체 생성시 초기 값 전달

    def __str__(self): # str() 비공식적 문자열
        return f'MyClass with value {self.val}' # 객체가 가진 값을 문자열로 출력 / 명시하지 않으면 주소로 리턴

    def __repr__(self): # repr()
        return f'Myclass (Value = {self.val})' ##객체가 가진 값을 서식을 만들어서 출력 / 명시하지 않으면 주소로 리턴


if __name__ == '__main__' :
    m1 = MyClass(1)
    ##__str__ 호출
    print(m1)
    print(str(m1))
    ##__repr__ 호출
    print(repr(m1))

