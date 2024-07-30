import traceback
def f1(a,b):
    return f2(a) + f2(b)

def f2(x):
    return  1.0/x

if __name__ == '__main__':
    try:
       f1(1.0,0.0)
    except (ZeroDivisionError , IOError) :  # 여러 개의 예외 클래스를 () 지정 할 수 있다.
        pass
        traceback.print_exc()
