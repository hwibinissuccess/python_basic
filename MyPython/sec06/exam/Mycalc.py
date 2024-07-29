# 두수(a,b)를 받아서 4칙연산을 구현하는 클래스를 만들고 싶다.
class  Calc:
    def __init__(self, a=10, b=10): #매개 인자 있는 명시된 생성자    c1= Calc() /  c2= Calc(100) / c3= Calc(3,4)
        self.a = a
        self.b = b

    def getHap(self):
        return self.a + self.b

    def getSub(self):
        return self.b  - self.a

    def getMul(self):
        return self.a * self.b

    def getDiv(self):
        return self.b  / self.a

    def __str__(self):    # c1   ==  c1.__str__()  /  c2 == c2__str__()  / c3 == c3__str__()
        return   f'{self.a}  + {self.b}  = {self.getHap()} \n' +   \
                 f'{self.b}  - {self.a}  = {self.getSub()} \n' +   \
                 f'{self.a}  * {self.b}  = {self.getMul()} \n' +   \
                 f'{self.b}  / {self.a}  = {self.getDiv():5.1f} \n'



