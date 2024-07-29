class MyScore:
    def __init__(self,kor,eng):
        self.kor =kor
        self.eng= eng
    def getTot(self):
        print("선조")
        return(self.kor + self.eng)


class MyScore02:
    def __init__(self,mus, che):
        self.mus =mus
        self.che= che
    def getTot(self):
        print("선조")
        return(self.mus + self.che)
class MyScore_Sub(MyScore, MyScore02):
    def __init__(self, kor,eng,mus,che,mat):
        super().__init__(kor,eng)
        #MyScore.__init__(self, kor, eng)
        MyScore02.__init__(self,mus, che )
        self.mat=mat
    def getTot(self):
        print("후손 메소드")
        return (MyScore.getTot(self)+ MyScore02.getTot(self) + self.mat) #후손이 선조의 동일한 이름의 메소드를 호출한 것

if __name__ == '__main__':
    #print(MyScore(20,30).getTot())
    print(MyScore_Sub(100,100,100,100,100).getTot()) #상속시에 재정의된 후손의 메소드가 호출된다.

