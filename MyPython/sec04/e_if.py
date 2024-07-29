#파이선 if~ elif~ else 의 변형 코드
def case01():
    score = int(input("점수  : "))
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


def case02():
    score = int(input("점수  : "))
    if score >= 90:
        grad = 'A'
    elif  score <= 89 and score >= 80:
        grad = 'B'
    elif score <= 79  and score >= 70:
        grad = 'C'
    elif score <= 69  and score >= 60:
        grad = 'D'
    else:
        grad = 'F'
    print(f'{score}의 학점은 {grad} 이다 ')


def case03():
    #<true_value> if <condition> else (false_value)
    #1.숫자가 짝수인지 홀수인지 출력  su % 2== 0
    su = 10
    res  = "짝수" if su  % 2 == 0 else "홀수 "
    print(res)
    #2. 나이가 18세 이상이면 성인 그렇지 않으면 미성년자라고 출력 하자.
    age  =18
    res  ="성인 " if  age >= 18 else "미성년자 "
    print(res)
   #3.  두수 중 최대 값을 리턴하자.
    a= 10
    b= 22
    max_value  = a if a > b else b
    print(max_value)


def case04():  # 127 삼항 연산자  적용
    score = int(input("점수  : "))
    grad  =  (
        'A'  if score >= 90  else
        'B'  if   80 <=   score < 90         else
        'C'  if score <= 79  and score >= 70 else
        'D'  if score <= 69  and score >= 60 else
        'F'
    )
    print(f'{score}의 학점은 {grad} 이다 ')


if __name__ == '__main__':
    case04()



