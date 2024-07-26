# int 클래스를 상속받아 홀수판별, 짝수 판별하는 기능을 추가해보자

class MyInt(int):
    #기능확장
    def is_even(self):
        return self%2 == 0

    def is_odd(self):
        return self%2 == 1

if __name__ == '__main__':
    my_number = MyInt(10)
    print(f'is even ? {my_number.is_even()}')
    print(f'is odd ? {my_number.is_odd()}')