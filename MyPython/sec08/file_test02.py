#2진화 코드   encoding, decoding
# [질문1 ]  스트림과 리얼타임 처리는 같은 개념인가요 ?
#        데이터 연속 흐름(바이트 통로)과  실시간 데이터 이벤트 처리 이다.
#     ex) 스트림 데이터를 실시간으로 처리하는 상황
#[질문 2] 만약 하트 비트로 체크를 안하면 사용자가 뭔가를 요청해도 응답이 없게 되는 건가요?
# 해야됨, 안 할 수가 없음
import sys  # -> sys.getdefaultencoding() 문자열 인코딩확인   , sys.getfilesystemencoding() 파일 인코딩 확인
class BTest:
    def b_wrtie(self):
        f = open("file_test02.txt",'wb')
        str ='대한민국 우리나라'
        f.write(bytes(str,'utf-8')) # 1byte 이내 코드값 변환   ASCII   ,  (확장형 코드 =  scan code , unicode)
        #f.write(str)
        f.close()

    def b_read(self):
        f= open("file_test02.txt","rb")
        while   True:
            s = f.read(1)
            if s ==b'':
                break
            print(s.hex(), s)
        f.close()
    def b_mread(self):
        with  open("file_test02.txt","rb")  as f :
            m =f.read().decode('utf-8')
            print(m)


if __name__ == '__main__':
    b1= BTest()  #기본 생성자를 호출하면서 객체를 생성한다.  __init__(self)
    b1.b_wrtie()
    b1.b_read()
    b1.b_mread()
    print(sys.getdefaultencoding())
    print(sys.getfilesystemencoding())
    print(sys.gettrace())
