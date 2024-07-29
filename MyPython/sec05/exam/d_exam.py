def test01():
     #def my():  return 100
     res  = lambda : 100
     print(res, res())
def test02():
    res=  lambda  x: 100+x
    print(res(10))

def test03():
    res = lambda  x,y,z: x+y+z
    print(res(1,1,1))




def test04():
    my_list   =[1,2,3,4,5]
    res  = lambda   x: x
    print(res(my_list ))

def  my(my_list):
    even_res   =  [  x  for x in my_list if  x % 2 ==0   ]
    return even_res

def test05():
    my_list = [1, 2, 3, 4, 5]
    res = lambda my_list: [  x  for x in my_list if  x % 2 ==0   ]    #x의 값 중 짝수만 리턴 해보자.
    print(res(my_list))


if __name__ == '__main__':
      test05()
