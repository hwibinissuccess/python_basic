''''
   1. .MyScore :
       Score   : 이름 국어 영어  수학  총점 평균 출력 메소드
       MyScore  :Score를 상속받아  5과목 국어, 영어, 수학, 음악 체육  (MUS,PE)을 총, 평균, 학점

    2. sec04.exam02.Score에서 호출을 해서 객체 배열을 만들어서 접근해 보자.
'''
from sec06.exam.Score import  *

class MyScore(Score):
     # 1. 생성자로 매개 인자 받아 선조에게 전달
     def __init__(self, name, kor, eng, mat, mus, pe) -> None:
         super().__init__(name, kor, eng,mat)
         self.mus = mus
         self.pe  = pe
     def getTot(self): #  2.getTot() 재정의
         return super().getTot() + self.mus+ self.pe  # 선조의 3과목 총점 + 내꺼 2과목

     def getAvg(self):
         return self.getTot() / 5.  # 내꺼 5과목의 총점  / 5

     #3.__str__ 출력
     def __str__(self):
         return  (f'{self.name:<5} {self.kor:5d}  {self.eng:5d} {self.mat:5d} {self.mus} {self.pe} '
                  f' |super: {super().getTot()}      | self :  {self.getTot()} '
                  f' |super: {super().getAvg():5.1f} | self:  {self.getAvg():5.1f} '
                  f' |super: {super().getGrade() }   | self:  {self.getGrade()}')


if __name__ == '__main__':

    my_list = [MyScore('홍길동1', 100, 100, 100, 100,100),
               MyScore('홍길동2', 90, 90, 90,100,100),
               MyScore('홍길동3', 80, 80, 80,100,100)]

    list(map(lambda  x: print(x) , my_list ))

