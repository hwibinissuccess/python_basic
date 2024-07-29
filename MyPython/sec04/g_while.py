##### 입력된 숫자들의 합을 구하는 코드를 작성해 보자.
# - 사용자가  0 을 입력하면 루프를 종료하자.

sum =0
while True: # 무한루프시작   제어변수
    # 숫자를 입력 받기
    user_input  = int(input("su : "))
    if user_input  == 0:
        break
    #입력값이 0이 아니면 합을 추가
    #sum  = sum + user_input
    sum += user_input

#결과 확인
print  (f'입력한 숫자의 합  :{ sum }')