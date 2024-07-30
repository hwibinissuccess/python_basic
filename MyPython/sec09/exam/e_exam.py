### 5. 예외 발생 시켜보자 : raise
def check_positive(num):
    if num < 0:
        raise ValueError("음수는 허용되지 않는다!")
    return num

try:
    check_positive(-1)
except ValueError as e:
    print(e)