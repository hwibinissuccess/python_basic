class MyClass :
    pass

if __name__ == '__main__' :
    m1 = MyClass()
    m2 = MyClass()
    m3 = MyClass()
    print(f'id로 출력 : {id(m1)} {id(m2)} {id(m3)}') #각 다른 주소에 생성된 독립된 인스턴스
    print(f' 객체의 기본 문자열 출력 주소로 : {m1} {m2} {m3}')
    print(f' 인터프린터 스크립트 실행 확인 : {MyClass.__name__} {MyClass.__base__}')