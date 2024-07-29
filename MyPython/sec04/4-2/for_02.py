# for  List of numbers 1~10 's sum
# for ~ else  :for 반복문의 수행이 끝나면 else구문이 실행된다.
# 1~ 10까지 나열된 값을 출력하고 합을 구하자.
# 1+2+3+~~   10= 55  / 만일에 val이 10이면  end=을 출력하고 나머지는  +를 출력하자.
def case01():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    m_sum = 0
    for val in numbers:
        if val == 10:
            print(val, end ='=')
        else:
            print(val, end ='+')
        m_sum = m_sum+val  # m_sum += val
    else:
        print(m_sum)

def case02():  #(1+2)*(3+4)*(5+6)*(7+8)*(9+10) / 1부터 10까지의 숫자를 포함해서 패턴을 만들어 곱을 결과를 리턴
    res  = 1
    my_v = ""
    for i  in range(1,11,2):
        if i + 1  <= 10:
            my_v +=  f"( {i} + {i+1} )*"
            res *=   (i + (i+1))

    print(my_v[:-1],'=', res )

def case03():  #(1/2)+(3/4)+(5/6)+(7/8)+(9/10)   => 번외  (1+2)* (3/4) ...
    # 1~10까지의 홀수와 그다음 짝수를 분자로 하고, 다음 짝수를 분모로 하는 분수의 합
    res = 0
    my_v = ""
    for i in range(1, 11, 2):
        if i + 1 <= 10:
            my_v += f"( {i} / {i + 1} )+"
            res += (i / (i + 1))

    print(f'{my_v[:-1]} = {res : .6f}')
if __name__ == '__main__':
    case03()
