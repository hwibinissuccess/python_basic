### <<Exception에서 사용할 수 있는 메소드, 속성, 목록을 표현하는 멤버>>
import trace
def test01():
    try:
        raise ValueError("오류 메시지")
    except ValueError as e:
        #print(e)
        e.add_note("추가 오류 정보")
        raise


def test02():
    try:
        raise ValueError("오류 메시지 잘못된 값 ", 44)
    except ValueError as e:
        print(e.args) # 출력결과 (튜플)

def test03():
    try:
        raise ValueError("오류 메시지")
    except ValueError as e:
        tb = e.__traceback__
        print("처리 중 오류 발생", tb)
        raise e.with_traceback(tb) # 예외의 원인, 발생위치 추적 #import trace 하기

if __name__ == '__main__':
    test03()

