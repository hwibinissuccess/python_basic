from datetime import datetime


def case01(score):
    if score >= 90:
        grad = 'A'
    elif score >= 80:
        grad = 'B'
    elif score >= 70:
        grad = 'C'
    elif score >= 60:
        grad = 'D'
    else:
        grad = 'F'

    print(f'{score}의 학점은 {grad} 이다 ')

def  case02(date_str):
    #날짜를 입력받아,날짜가 토요일인지 일요일이지 평일인지 구현해보자.  if - elif- else
    #입력된 문자열을 datetime객체로 변환
    input_date  = datetime.strptime(date_str,"%Y-%m-%d")

    #요일 계산 (0:월요일, 6:일요일)
    weekday  = input_date.weekday()

    #요일인지 일요일이지 평일인지 구현해보자.  if - elif- else
    if  weekday  == 5 :
        day_type  ="토요일이다. "
    elif weekday == 6  :
        day_type  ="일요일이다."
    else:
        #day_type ="평일이야. "
        day_type = f"{input_date.strftime('%A')} (weekday) "

    print (f' {input_date.strftime('%Y-%m-%d')}는  {day_type} ')

if __name__ == '__main__':
    #score  =  int(input("점수  : "))
    #case01(score)
    ################### case02
    #날짜를 입력 받자.
    date_str  = input("날짜를 입력 해봐 (YYYY-MM-DD): ")
    #조건함수 호출
    case02(date_str)









