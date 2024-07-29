from dataclasses import make_dataclass, field
from typing import Any

# 동적으로 dataclass 생성
my_score = make_dataclass(  'Score',
                       [
                        ('name', str, field(default='noname ')),
                        ('kor', int, field(default=0)),
                        ('eng', int, field(default=0)),
                        ('mat', int, field(default=0))
    ],
    init=True,
    repr=True,
    namespace={
        '__post_init__':lambda self:setattr(self,'name' , self.name.strip()),
        'getTot':lambda  self:self.kor + self.eng + self.mat,
        '__str__':lambda self:f'{self.name:<5} {self.kor:5d} {self.eng:5d} {self.mat:5d}'
    }
)
if __name__ == '__main__':
    my_all = [
        my_score(" 홍길동 ", 90, 80, 70),
        my_score("정길동", 50, 60, 70),
        my_score("이길동", 100, 100, 100)
    ]

    # __post_init__ 메서드를 호출하기 위한 코드
    for res in my_all:
        res.__post_init__()

    print("====. 홍길동의 이름을 박길동으로 / 국어 100 변경해서 s1의 객체만 출력 ====== ")

    for res in my_all:
        if res.name == "홍길동":  # 문자열 양쪽 공백 제거
            res.name = "박길동"
            res.kor = 100
            print(res)  # __str__()
            print(f" tot  =  {res.getTot()}")
            print(repr(res))  # __repr__() 호출
            print(res.__repr__())
            break  # 홍길동 찾은 후 이름 변경 루프 종료

