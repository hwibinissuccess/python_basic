#datetime 모듈을 추가해서  활용해 보자.

from datetime import datetime,date

def case01():
    #현재 날짜와 시간
    current_datetime  = datetime.now()
    print(f'날짜와 시간 {current_datetime}')

    #현재 날짜
    current_date  = date.today()
    print(f'현재날짜 {current_date}')

def case02():
    #입력 받는 문자열의  날짜 datetime.strptime(string,format) .strftime(format)가 주말인지  아닌지 판별 해보자.
    date_str  = input("Enter a date (YYYY-MM-DD):  ")
    date_obj    = datetime.strptime(date_str , "%Y-%m-%d") #문자열을 서식에 맞게  datetime으로 리턴
    print(type(date_str) , type(date_obj))
    if date_obj.weekday()  >= 5 :#5=토요일   6= 일요일
        print(f'{date_str}은 주말이야 ')
    else:
        print(f'{date_str}은 평일이야 ')

def case03():
    from datetime import timedelta #기간 중에 시간계산
    delta = timedelta(
        days=50,
        seconds=27,
        microseconds=10,
        milliseconds=29000,
        minutes=5,
        hours=8,
        weeks=2
    )
    #현재 날짜 시간
    now = datetime.now()
    #시간 계산
    f_date  = now + delta
    print("현재 날짜  : " , now)
    print("예약 시간  : ", f_date)
    print(delta)
    res =datetime.strptime('31/01/22 23:59:59.999999','%d/%m/%y %H:%M:%S.%f')
    print(res)

def case04():
    from dateutil.relativedelta import relativedelta  #날짜간의 계산을 쉽게 하겠다.
    #오늘 날짜 에서 종강까지 몇년 몇월 몇일 몇시간 남았을까?
    #오늘 날짜.
    today = datetime.now()

    #종강 날짜.
    target_date  = datetime(2025,1,10)

    #날짜 차이 계산
    res  = relativedelta(target_date,today )
    print(res)
    print(f' {res.months} 개월  { res.days}일 , {res.hours} 시간이 남았다.  ')
    print( target_date - today )

def case05():
    import calendar
    #2024년도 달력을 출력하자.
    print(calendar.calendar(2024))
    print("=====================")
    #2024년도 7월 달력을 출력해줘
    print(calendar.month(2024,7))
    #weekday()를 통해서 특정 날짜의 요일을 리턴해줘
    print(calendar.weekday(2024, 7,22))    #0월요일  6일요일
    # setfirstweekday(firstweekday)를 사용해서 일요일 부터 시작 하고 싶다.
    calendar.setfirstweekday(calendar.SUNDAY)
    print(calendar.month(2024, 7))


if __name__ == '__main__':
    case05()


