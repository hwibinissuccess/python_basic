# 이름, 주소 , 전화번호를 관리하는 Address라는 클래스를 만들어 보자
'''
 name   addr  tel
 홍길동 서울    111111   a1
  정길동 인천   222222  b1
 박길동 구미    333333   c1
'''
class Address:

    def __init__(self, name, addr, tel):
        self.name = name
        self.addr  = addr
        self.tel   = tel

    def __str__(self):
        res  = f' {self.name:10s}  {self.addr:10s}  {self.tel:10s} \n'
        return res

if __name__ == '__main__':
    a1  =  Address("홍길동","서울" ,"111111")
    b1=  Address("정길동" ,"인천" ,"222222")
    c1= Address ('박길동' ,"구미" ,"333333")
    print(a1,b1,c1)


