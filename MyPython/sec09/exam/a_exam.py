try:
    # 예외 발생할 수 있는 코드
    ans=10*(1/2)
except ZeroDivisionError:
    # 예외 처리
    print("0으로 나눌 수 없어")

else:
    # 예외가 발생되지 않을 경우 실행되는 코드
    print("정상적으로 실행 완료 :",ans)

