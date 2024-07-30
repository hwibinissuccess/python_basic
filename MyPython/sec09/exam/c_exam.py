### 3. 예외 객체 : 객체에 대한 정보를 출력하고 싶을 경우
try:
    ### 예외가 발생할 수 있는 코드
    10*(1/0)
except ZeroDivisionError as e : ### 별칭 e = ZeroDivisionError('division by zero')
    ### 예외처리
    print(f"예외가 발생 되었다 : {e.__str__()}")

    