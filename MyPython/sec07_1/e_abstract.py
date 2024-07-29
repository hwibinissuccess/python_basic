from abc import ABCMeta, abstractmethod
class Base(metaclass=ABCMeta) : # 난 객체 생성 안하는 추상클래스 . 단, 후손에게 강제로 추상메소드를 재정의 시킨다.

    #추상화 @을 함수위 에 지정할 수 있다.
    @abstractmethod   #추상메소드
    def start(self):
       pass
    @abstractmethod
    def stop(self):
        pass

class Cat(Base) :
    def start(self):
        print('Cat  start')
    def stop(self):
        print('Cat stop')


class Duck(Base) :
    def start(self):
        print('Duck  start')
    def stop(self):
        print('Duck stop')




class Puppy(Base):
    def start(self):
        print('Puppy  start')

    def stop(self):
        print('Pyppy stop')

def my_class(m :  Base ):  #정적타입 명시
     m.start()
     m.stop()
def my_class(r ):    # 동적 타입
    r.start()
    r.stop()
if __name__ == '__main__':
    my_class(Cat())   #Base <- Cat
    my_class(Duck())  #Base  <- Duck
    my_class(Puppy()) #Base  <- Puppy
    #my_class(Base())



