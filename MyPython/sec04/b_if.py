#ex)만일에 입력받은 문자가 소문자이면      '소문자',  그렇지 않을 경우     '소문자가 아니야'를 출력하자.
def case01():  #islower(self, /) unbound builtins.str method
    input_str  = input("input str :")  # type(input_str) == str
    if  input_str.islower()    :  # inpust_str의 메소드 호출
        print('소문자')
    else:
        print('소문자가 아니야')


#ex)만일에 입력받은 문자가 소문자이면 출력하고 대문자로 변환하고, '소문자 아니야'를 출력하자.
def case02():
    input_str = input("input str :")  # type(input_str) == str/  input_str  = str( input("input str :")  )
    if input_str.islower():  # inpust_str의 메소드 호출
        print('소문자')
        print(f'{input_str} 대문자로 변환  : {input_str.upper()}')
    else:
        print('소문자가 아니야')

def case03():  #짝수 홀수 판별을 해보자.   su  % 2 == 0
    su  =  int(input ('input su ====> '))
    if  su % 2 ==  0 :
        print(f'{su} 는 짝수야  ')
    else:
        print(f'{su}는 홀수야 ')

def case04(): # 연도를 판별해서 윤년 확인
    #(연도가 4로 나누어 떨어지면 윤년 and 100으로 나누어 떨어지면 윤년이 아님 ) or  연동가 400으로 나누어 떨어지면 윤년)
    year= int(input('input year ====> '))
    if (year % 4 ==0  and year % 100 != 0  ) or (year % 400  ==  0 ) :
        print(f'{year} 는 윤년 ( leap year) 이야 ')
    else:
        print(f'{year} 는 윤년 ( leap year) 아니야  ')



if __name__ == '__main__':
    case04()
