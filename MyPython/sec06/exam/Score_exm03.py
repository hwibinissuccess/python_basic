#python 권장 클래스 원형
from dataclasses import dataclass
from typing import Any
@dataclass(init=True, # __init__ 자동생성
           repr=True, # __repr__ : 클래스가 가지고 있는 특성을 리턴, print or repr(객체변수) 같이 사용해야함
           eq=True, # __eq__ : 두객체 같은지 다른지 비교
           order=False, # 비교 연잔들을 다 만들어줌 -> __lt, __le__, __gt__, __ge__
           unsafe_hash=False, # __hash__ -> eq, unsafe_hash, frozen을 다 true로 해서 객체를 불변으로 해서 사용, 그래야 안전한 hash값을 쓸 수 있음
           frozen=False, # 객체 불변 -> 필드 속성값을 읽기 전용으로 만들겠다.
           match_args=True, # {a-z} (a~z 맞아?) 등 패턴 확인, __match_args__ 자동생성 / ver 3.10 이상
           kw_only=False, # 속성 키워드 전용 지정(생성자로 값을 받을 때 선택적으로 사용)
           slots=False, # __slots__, 메모리 사용을 줄이겠다, 최소로 쓰겠다,메모리 액세스는 하지만 추가는 하지 않겠다. 메모리 사용 줄임!!!, 메모리 사용 더이상 안하겠다.read만 빠르게, cud는 안하겠다.
           weakref_slot=False) # 메모리 최적화, 객체에 따라 약한 참조를 하겠다, 위 slots랑 같이 써야함
class Score:
    name: str
    eng: Any
    kor: int
    mat: int = 100 # 기본값 있는 필드는 맨 밑에, 아니면 오류남

    def getTot(self) -> int:
        return self.kor + self.eng + self.mat

# ----------------------------------- str, init 등 자동으로 생성됨.

    def __str__(self):
        return f'{self.name:<5} {self.kor:5d}  {self.eng:5d} {self.mat:5d}'

if __name__ == '__main__':
    my_all  =[ Score(" 홍길동 ", 90, 80, 70) , Score("정길동", 50, 60, 70) , Score("이길동", 100, 100, 100) ]
    print( "====. 홍길동의 이름을 박길동으로 / 국어 100  변경해서 s1의 객체만 출력  ====== ")

    for res in my_all:
        if res.name.strip() == "홍길동": # 문자열 양쪽 공백 제거
            res.name="박길동"
            res.kor = 100
            print(res)  #__str__()
            print(repr(res))  ##__repr__()  호출
            print(res.__repr__())
            break  #홍길동 찾은후 이름변경 루프종료

