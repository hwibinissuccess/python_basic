class AA:
    def __init__(self, a= 0, b=0):
        self._a = a
        self._b = b
    def getHap(self):
        return self._a+ self._b

    #멤버변수 _a값 리턴
    def getA(self):
        return self._a

    # 멤버변수 _a값 전달 및 변경
    def setA(self, a ):
        self._a = a

    def getB(self):
        return  self._b

    def setB(self, b):
        self._b = b

    def __str__(self):
        return (f'{self._a:3d}  + {self._b:3d} '
                f'= {self.getHap():3d} ')
class BB(AA):

    def __init__(self, a=0, b=0, c=0):
        super().__init__(a, b)
        self._c = c
    def getC(self):
        return self._c

    def setC(self, c):
        self._c = c
    def getRes(self):
        return super().getHap()  * self._c

    def __str__(self):
        return f'({super().getA():3d}  + {super().getB():3d} )  * {self._c:3d}   = { self.getRes():3d} '


if __name__ == '__main__':
    my  = BB (100, 60 , 2) # BB 클래스의 생성자로 값전달
    print(my)  # my.__str__()  => BB's __str__()
    print(my.getA()  , my.getB() , my.getC())

    #my의 a값만 변경해서 결과를 출력 받자
    my.setA(200)
    print(my)



