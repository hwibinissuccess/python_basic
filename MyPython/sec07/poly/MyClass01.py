#super() : 선조 클래스를 의미한다. 명시적으로 후손 클래스에서 선조의 변수나 메소드를 참조할때 사용한다.
#후손클래스에서 후손이 가진 값을 선조 클래스의 생성자를 호출해서 대입하려면 super()키워드를 사용한다

#간단한  구조의 상속을  구현해 보자.
# 이름과 나이를 관리하는  Person 클래스있다.
# Student클래스 Person을 상속을 받아 학년만 추가해서  이름, 나이, 학년을 모두 출력하는 클래스를 만들고 싶다.
'''
  1. 상속관계  : 기능을 확장 / 재정의 / 단일상속 or  다중상속
  2. 생성자 호출  : 값전달 하면서 생성
  3. 객체 생성
'''
from inspect import  * # 모듈 객체 검사할때 사용하는 모듈 : 동적으로 생성된 클래스와 멤버 정보를 확인
class Person:
    __b = 10
    def __init__(self, name, age, b):
        self.name = name
        self.age = age
        self.__b=b
    def __repr__(self):
        return  f" {self.name } : (age :{self.age} )"

class Student(Person):
    def __init__(self,name, age,b, grade = 5 ):
       # Person.__init__(self,name,age) -> suer().이 아니라, 선조. 할 때는 self를 넣어줘야함
        super().__init__(name,age,b)
        self.grade = grade

    def __repr__(self):
        #print("b= " ,  self.__b)  -> 상속관계 라도 prvate은 호출 불가능
        return  f"{super().__repr__() },grade :{self.grade}"

if __name__ == '__main__':
    x=Student("Ruri",7,3,5)
    print(x)
    '''
     1. 클래스 객체 확인  
     2. 매개인자 확인  
     3. 상속 계층 확인  
    '''
    print( "1. 클래스 객체 확인  :", isclass(Student))
    print("2. 매개인자 확인  :" ,getfullargspec(Student))
    print("3. 계층관계 : " , getmro(Student))
    print("4, 모듈확인  :", ismodule(Student))
    print("5. 멤버 확인  :", getmembers(Student, predicate=ismethod))
    print("6. 소스확인 :", getsource(Student))
    print("7. Docs 확인 :", getdoc(Student))







