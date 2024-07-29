#from _typeshed import Self
from abc import abstractmethod, ABCMeta

'''
 ***추상메소드를 가진 클래스는 추상클래스가 되고 객체 생성 불가능 *** 
 (Can't instantiate abstract class AA without an implementation for abstract method 'prn')
  1)선조가 가진 추상메소드를 후손이 재정의하지 않으면 객체를 생성할 수 없다
  2)재 정의하지 않는 후손은 추상클래스를 된다.  

  Tip: 추상클래스란? 다형성과 동적 바인딩(다양한 형태의 성질(기능)을 가진 후손 클래스들을 추상 메소드로 통일 하는 구조 )
       - 추상클래스 객체 생성 불가, 후손 추상메소드 반드시 재정의, 재정의하지 않는 후손은 추상클래가 된다.   

'''
class My(metaclass=ABCMeta):
     #추상클래스 , 객체 생성 안하고[Can't instantiate] 후손 클래스에게 추상메소드를 강제로 재정의 하겠다.  !!!
     @abstractmethod
     def prn(self):  #추상 메소드  / 후손 강제 재정의하겠다.
         pass

     def test(self):
         print("중요한 메소드")
class  Test(My):
    def m(self):
        print(" Test'm  method' ")

    def prn(self):
        print("재정의 메소드 ")

if __name__ == '__main__':
    #m  = My()  # Can't instantiate
    t   = Test ()
    t.m()
    t.test()








