### from : 특정 예외를 다른 예외의 직접적인 원인으로 지정할 경우 사용 : 예외 체인
### ValueError가 발생되면 RuntimeError 예외의 원인으로 지정하여 새로운 예외를 발생
import traceback
from datetime import datetime
def test01():
    try:
        raise ValueError("잘못된 값입니다.")
    except ValueError as v:
        # raise # 현재 활성화된 예외를 다시 발생시킨다.
        # raise RuntimeError("런타임 오류 발생") from v
        with open('error_log.txt', 'a', encoding='utf-8') as file:
            file.write("예외 발생 \n")
            traceback.print_exc(file=file)  # 스택 트레이스를 파일에 기록
            file.write("\n")
        raise RuntimeError("런타임 오류 발생") from v


def test02(): ### 예외 메시지와 시간 기록까지 -> [년-월-일 00:00:00] 예외 발생 : 예외메시지
    try:
        raise ValueError("잘못된 값입니다.")
    except ValueError as v:
        # raise # 현재 활성화된 예외를 다시 발생시킨다.
        # raise RuntimeError("런타임 오류 발생") from v
        with open('error_log2.txt', 'a', encoding='utf-8') as file:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{now}] 예외발생 : {v} : {v.__class__.__name__}\n")
        try:
            raise RuntimeError("런타임 오류 발생") from v
        except RuntimeError as res:
            with open('error_log2.txt', 'a', encoding='utf-8') as file:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"\t ===> [{now}] 예외발생 : {res} : {res.__class__.__name__}\n")
            raise

if __name__ == '__main__':
    test02()


