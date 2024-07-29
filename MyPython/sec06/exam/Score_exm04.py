#python 권장 동적 클래스 원형
from dataclasses import make_dataclass, field
from typing import Any

my_score  = make_dataclass('Score',
                           [
                               ('eng', int, field(default=0)),
                               ('mat', int, field(default=0)),
                               ('kor', int, field(default=0)),
                               ('name' , str,field(default='noname')),
                           ],
                           init=True,
                           repr=True
)

# 생성된 dataclass에 초기화 메소드를 추가, 객체, 메소드로 호출해야 실행되는 메소드
def __post_init__(self):
    # 사용자가 추가적인 초기값 지정
    self.name = self.name.strip()

def __str__(self):
        return f'{self.name:<5} {self.kor:5d}  {self.eng:5d} {self.mat:5d}'
def getTot(self):
        return self.kor + self.eng + self.mat

#동적으로 생성된 dataclass에 추가,
my_score.__post_init__ = __post_init__
my_score .__str__= __str__
my_score .myTot =  getTot

if __name__ == '__main__':
    my_all  =[ my_score(" 홍길동 ", 90, 80, 70) , my_score("정길동", 50, 60, 70) , my_score("이길동", 100, 100, 100) ]
    print( "====. 홍길동의 이름을 박길동으로 / 국어 100  변경해서 s1의 객체만 출력  ====== ")

    for res in my_all:
        if res.name.strip() == "홍길동": # 문자열 양쪽 공백 제거
            res.name="박길동"
            res.kor = 100
            print(res)  #__str__()
            print(f" tot  =  {res.myTot()}")
            print(repr(res))  ##__repr__()  호출
            print(res.__repr__())
            break  #홍길동 찾은후 이름변경 루프종료

