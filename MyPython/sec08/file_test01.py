#2진화 코드분 / byte(이미지 , 영상, 소리, 네트워크 전송데이터) ,   char  ->open /   object (node) << 직렬화, 역직렬화 stream
# 임시기억장소  : 버퍼 (1byte), 클립보드(gui)  , 누산기(가산기 안에 있는 연산데이터 프로세싱 3+4 ) , 레지스터 (명령어)
# stream : byte 통로  (0,1= bit * 8  = 1byte)
class BTest:


    def __init__(self):
        self.__file = "res/file_test01.txt"

    def b_wrtie(self):
        with open(self.__file,'wb') as f:  # 바이너리로 파일에 쓰겠다.
            f.write(b'ABC123') # 1byte 이내 코드값 변환   ASCII   ,  (확장형 코드 =  scan code , unicode 2byte= 0~ 65535)

    # 키보드 버퍼  ->   [버퍼링] stream (IO)   - > 파일
    def b_read(self):
        f= open("res/file_test01.txt","rb")
        while   True:
            s = f.read(1)
            if s ==b'':
                break
            print(s.hex(), s)
        f.close()

if __name__ == '__main__':
    b1= BTest()  #기본 생성자를 호출하면서 객체를 생성한다.  __init__(self)
    b1.b_wrtie()
    b1.b_read()
