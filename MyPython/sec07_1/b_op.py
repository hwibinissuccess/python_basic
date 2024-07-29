#### 연습 : 자료형을 확장해보자, UI  확장 , 속성 정의 확장
class MyList(list):
    #기능추가
    def sum(self):
        return sum(self)#합을 구하는 내장 함수를 호출
    def average(self):
        return  sum(self) /len (self)

if __name__ == '__main__':
    mlist  = MyList([1,2,3,4,5])  #list(iterable=(), /)
    print(dir(mlist))
    print(mlist, type(mlist))
    print(f' sum :  {mlist.sum()}')
    print(f'average : {mlist.average()}')


