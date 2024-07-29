import math

def test01() : #매개인자와 리턴이 없는 경우
    print('a_exams fun')
    print('%20s'%('a_exams fun')) # %d %o %x %f %s %e
    print('{0} {1}'.format("a_exam's", " fun"))

def test02(angle_degrees) : # 매개인자가 있고 리턴이 없는 경우
    # math 모듈을 이용해서 삼각함수와 고나련된 계산을 수행하자! 각도를 입력받아 사인, 코사인, 탄젠트를 계산해서 출력

    a_r = math.radians(angle_degrees)

    #### 계산
    s = math.sin(a_r)
    c = math.cos(a_r)
    t = math.tan(a_r)

    #### 출력
    print(f"Sine of {angle_degrees}' degress :{s: 5.2f}")
    print(f"Cosine of {angle_degrees}' degress :{c: 5.3f}")
    print(f"Tangent of {angle_degrees}' degress :{t:5.4f}")

def test03() : # 매개인자는 없고 리턴이 있는 경우 / 짖어된 숫자를 판별해 리턴 받기
    return isinstance(100, (int, float))

def test04(num, char) : #매개인자와 리턴이 있는 경우 / int() str() isinstance()
    # 1. 숫자와 문자를 입력받아 판정하고 숫자는 문자로 변환하고, 문자는 수자로 변환해보자
    # 2. 각 변환한 것을 리턴해보기
    if isinstance(num, (int, float)) :
        num_as_str = str(num)

    if isinstance(char, str) :
        str_as_num = int(char)

    return num_as_str, str_as_num

if __name__ == '__main__' :
    #test01() #a_exam's fun
    #test02(15)
    #print(test03())
    print(f'{test04(100,'200')}')