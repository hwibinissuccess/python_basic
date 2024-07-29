'''
===> 이름,국어,영어, 수학을 입력받아  총점, 평균, 학점을 출력하는 클래스
 [1] 모든 속성을 public
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
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getTot(self):
        return self.kor + self.eng + self.mat
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
    def __str__(self):  #object 'class의 메소드를  재정의
        return (f'{self.name:<5} {self.kor:5d}  {self.eng:5d} {self.mat:5d}  {self.getTot()} '
                f' {self.getAvg():5.1f}  '
                f' {self.getGrade()}'
                f'  {super().__str__()}')  #후손은 super()라는 키워드를 통해서 선조의 메소드를 호출









