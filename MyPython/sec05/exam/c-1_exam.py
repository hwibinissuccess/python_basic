def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

if __name__ == '__main__':
    # outer_function 호출해서 클로저 생성
    closure_fun = outer_function(10)

    # __closure__ 속성을 사용해서 클로저 확인
    print(closure_fun.__closure__) # 함수가 캡처한 변수를 포함하는 tuple
    print(closure_fun.__closure__[0].cell_contents) # 캡처된 변수의 값
