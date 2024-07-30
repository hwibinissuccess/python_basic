class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls() # 현재 클래스의 인스턴스를 예외 발생 시킨다.
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")