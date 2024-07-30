### 4. 사용자 예외 설정 : 1. Exception을 상속받아 코드를 설계 / 2. raise 키워드 사용 = 예외 명시 발생
class MyError(Exception):

    #pass

    def __str__(self):
        return "현재 사용자 예외를 하고 있다."

try:
    raise MyError("사용자 정의 에러 발생가 발생")
except MyError as e:
    print(e) # e.__str__(), 생성자로 전달한 "사용자 정의 에러 발생가 발생"을 리턴 -> 오류 원인 문장 !!!
    print(dir(e)) #Exception의 메소드 및 속성들을 호가인