### c_ploy.py -> make_dataclasses 메소드로 동적 클래스를 생성해보기
from dataclasses import make_dataclass, field

# 동적 dataclass AA 생성
AA = make_dataclass('AA',
                    [ # init으로 들어가는 초기값
                        ('_a', int, field(default=0)),
                        ('_b', int, field(default=0))
                    ],
                    namespace = {
                        'getHap' : lambda self : self._a+self._b,
                        'getA' : lambda self : self._a,
                        'setA' : lambda self,a : setattr(self, '_a',a),
                        'getB' : lambda self : self._b,
                        'setB' : lambda self,b : setattr(self, '_b',b),
                        '__str__': lambda self : f'{self._a:3d}  + {self._b:3d} = {self.getHap():3d}'
                    }
)

# 동적 dataclass BB 생성 << 주의 : 람다 함수에서는 SUPER()를 직접 호출할 수 없다.
# 주의사항 : 2. RecursionError : 클래스 생성할 때 메소드가 동일하면 재귀적으로 호출하는 경우 => 메소드 이름을 다르게 지정 또는 클래스.메소드(self)로 명히호출
BB = make_dataclass('BB',
                    [
                        ('_c', int, field(default=0))
                    ],
                    bases=(AA,),
                    namespace={
                        'getC' : lambda self : self._c,
                        'setC' : lambda self, c : setattr(self, '_c',c),
                        'getRes' : lambda self : self.getHap()  * self._c, # AA.getHap(self)
                        '__str__' : lambda self : f'({self.getA():3d}  + {self.getB():3d} )  * {self._c:3d}   = { self.getRes():3d}'
                    }
)

if __name__ == '__main__':
    my = BB (100, 60 , 2) # BB 클래스의 생성자로 값전달
    print(my)  # my.__str__()  => BB's __str__()
    print(my.getA()  , my.getB() , my.getC())

    #my의 a값만 변경해서 결과를 출력 받자
    my.setA(200)
    print(my)



