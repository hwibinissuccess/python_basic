'''
List Comprehension : list 객체를 for문을 활용해서 연산결과를 list로 리턴

형식
[리턴값 for 변수 ,, in list 객체] -> return 키워드가 없다
[표현식 for 항목 in iterable if 조건] -> return 키워드가 없다
'''

def forTest():
    list1 = [1,2,3,4,5]
    print('1. 요소*요소 =>', [x*x for x in list1])
    print('2.(요소, 요소*요소) =>', [(x, x*x) for x in list1])
    print(f'3. 짝수만 요소*요소로 출력 => {[x*x for x in list1 if x%2 == 0]}')
    print('.요소*요소 =>', [x*x for x in range(1,6)])

    my_word = ['apple', 'watermelon', 'peach', 'pear']
    print('5. 문자열을 대문자로 변환 =>', [(x.upper(), len(x)) for x in my_word])

    n_list = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    rest_list = [num for sublist in n_list
                    for num in sublist]
    print('6. 중첩 연산: =>', rest_list)

def forTest01():

    number = range(1,11)
    print('1. 1~10까지 even, odd =>', ['even' if x%2 == 0 else 'odd' for x in number])
if __name__ == '__main__':
    forTest()