def Test():
        #목록을 한꺼 번에 묶어서 리턴 1,10: 2,20: 3,30으로 리턴 된다.
        # zip ( ,,,,,)  ->for로 풀어낸다.
        #목록에서 가장 짧은 객체를 기준으로 페어를 만든다.
        for x, y ,z in zip ([1,   2,  3,  4,   5,  6,  7,  8],
                            [10, 20, 30, 40, None ],
                            [11, 20, 33, 44, None  ] ) :
                print (f'{x}  :   {y}  : {z}' )
def Test01():
        #목록을 묶어서 set으로 리턴
        print("====> ", set(zip ( ['a', 'b', 'c','d'], [1, 2, 3, 4])))
        res  = set(zip ( ['a', 'b', 'c','d'], [1, 2, 3, 4]))
        print(type(res))
        print(res )

def Test02():
        #목록을 묶어서 dict로 리턴
        keys = ['cat', 'dog', 'duck']
        values = ['야옹', '멍멍', '꽥꽥']
        print (dict(zip(keys, values)))

if __name__ == '__main__':
    Test02()