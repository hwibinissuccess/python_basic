'''
===> 이름,국어,영어, 수학을 입력받아  총점, 평균, 학점을 출력하는 클래스
 [1] 모든 속성을 private으로 지정하고 각 속성값을  변경 및 전달 (setter), 리턴하는 구조(getter)를
      @property 데코레이터로 구현하자.
 [2] 초기값을 자동으로 생성하지 않고 객체에 생성시  값을 받아서 초기화
 [3] 평균은 소수이하 한자리 출력하자.
 [4] 학점은 A~  F 까지 설정한다.


name   kor  eng  mat   tot  avg  grad=> Score
홍길동   90    80   70                 = > s1
정길동   50    60   70                 => s2
이길동   100  100   100                 => s3
'''

class Score:  # 클래스에서 멤버는 self
    def __init__(self, name, kor, eng, mat) -> None:  # 객체를 생성할 때 값을 받으면서 생성 하겠다.(초기값을 자동으로 생성하지 않고 받아서 초기화)
        self._name = name
        self._kor = kor
        self._eng = eng
        self._mat = mat
    #################################################
    @property  #getter  값을 리턴
    def name(self):
        return self._name

    @name.setter  # 이름 값 전달 및 변경
    def name(self,name):
        self._name = name
    ###############################################
    @property  # kor()를 변수처럼 kor로 쓰겠다.
    def kor(self):
        return self._kor

    @kor.setter   #kor 값을 전달 및 변경하겠다.
    def kor(self, kor):
        self._kor = kor


    ##############################################
    @property
    def eng (self):
        return  self._eng

    @eng.setter
    def eng(self, eng):
        self._eng = eng


    ##############################################
    #수학 값 전달 및 변경
    @property
    def mat(self):
        return self._mat

    @mat.setter
    def mat(self, mat):
        self._mat  = mat

    #############################################

    def getTot(self):
        return self._kor + self._eng + self._mat
    def getAvg(self):
        return  self.getTot()/ 3.
    def getGrade(self):
        avg = self.getAvg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        else:
            return 'F'

    ## __str__ 추가
    def __str__(self):
        return (f'{self._name:<5} {self._kor:5d}  {self._eng:5d} {self._mat:5d}  {self.getTot()}  {self.getAvg():5.1f}  '
                f' {self.getGrade()}')



if __name__ == '__main__':
    my_all  =[ Score(" 홍길동 ", 90, 80, 70) , Score("정길동", 50, 60, 70) , Score("이길동", 100, 100, 100) ]
    print( "====. 홍길동의 이름을 박길동으로 / 국어 100  변경해서 s1의 객체만 출력  ====== ")

    for res in my_all:
        if res.name.strip() == "홍길동": # 문자열 양쪽 공백 제거
            res.name="박길동"
            res.kor = 100
            print(res)  #__str__()
            break  #홍길동 찾은후 이름변경 루프종료








