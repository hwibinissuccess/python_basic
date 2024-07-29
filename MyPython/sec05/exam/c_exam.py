def test():
     def my_inner():
            return 100
     return my_inner

def test01(a):
    b  =[1,2,3,4,5]
    def my_inner():
        return 100*a + b[a]
    return my_inner

def quadratic( a, b, c ):
    cache = {}
    def f( x ):
         if x in cache:
            return cache[x]
         y = a * x * x + b * x + c
         cache[ x ] = y
         return y
    def mytest():
        return 99999
    return f

if __name__ == '__main__':
    f1 = quadratic(3, -4, 5);
    print(f1)
    print(f1(3))
    print("========================================")
    res = [cell.cell_contents for cell in f1.__closure__] # 함수의 클로저 : 함수 내부에서 정의된 함수가 outer 함수의 변수를 참조하는 경우에 생성
    print(res)