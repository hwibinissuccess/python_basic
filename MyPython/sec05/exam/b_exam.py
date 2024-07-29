
def myFunc(*a): # 0 or more -> tuple
    print(a)

def myFunc01(*a,b=10):  #print(*args, sep=' ', end='\n', file=None, flush=False)
    print(f'a={a} b={b}  ')

def myFunc02(*a, **d): # **d 변수는 앞에 토플변수를 두고 마지막 순서에 명시 #초기값이 없는 이상!
        print(f'tuple={a} dict={d} ')


def myFunc03(*a, b=10,  **d):
    print(f'tuple={a} b={b} dict={d} ')

if __name__ == '__main__':
   ''' 
   myFunc02(1,2,3,4, z = 100, y=200 )
   mytuple=(1,2,3,4,5)
   mydict ={'a':1, 'b':2}
   myFunc02(*mytuple, **mydict)
   '''
   myFunc03(1, 2, 3, b=4, z=100, y=200)