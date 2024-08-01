import json
from datetime import datetime
### 복소수를 json 형식으로 인코딩
### Json이 복소수 타입을 제공하고 있지 않기 대문에 사용자 인코더를 정의해서 사용

def test01():
    class ComplexEncoder(json.JSONEncoder):  # 1. 상속 후 어떤 데이터가 대입되도 복소수 객체를 처리하겠다.
        def default(self, obj):  # 오버라이드 : 메서드 재정의
            if isinstance(obj, complex):
                return [obj.real, obj.imag]  # 복소수 타입이라면 실수, 허수를 리스트 타입으로 리터
            return super().default(obj)

    res = json.dumps(2 + 1j, cls=ComplexEncoder)
    print(f"1 {res}")
    res = ComplexEncoder().encode(2 + 1j)
    print(f"2 {res}")
    res = list(ComplexEncoder().iterencode(2 + 1j))
    print(f"3 {res}")

# 'datetime' 객체를 json 형식으로 인코딩 해보기
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime): # obj가 datetime 객체라면
            return obj.isoformat()    # ISO 포맷형식으로 변환해서 리턴하자
        return super().default(obj)

def test02():
    # 현재 시간을 datetime 객체를 생성
    current_time = datetime.now()

    # json.dumps()를 사용해서 json 문자열로 인코딩
    json_str = json.dumps(current_time, cls=DateTimeEncoder)
    print(json_str)

    # DateTimeEncoder 인스턴스 사용해서 인코딩
    res = DateTimeEncoder().encode(current_time)
    print("결과 : ", res)

    # DateTimeEncoder 인스턴스 사용해서 Iterator로 인코딩
    res = list(DateTimeEncoder().iterencode(current_time)) # 토큰화
    print(res)

    '''
    {"name" : "홍길동", "addr":"서울시", "tel":"02-0000"} -> 토큰
    {"name" : "홍길동", "addr":"서울시", "tel":"02-0000"} -> iterator -> __iter__ / __next__
    iterator()의 목적 : 메모리 절약(), 스트리밍
    '''

if __name__ == '__main__':
    test02()