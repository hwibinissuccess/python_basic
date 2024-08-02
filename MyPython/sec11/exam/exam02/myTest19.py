from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap  # class Counter(builtins.dict)
def test01():
    #ex) 클로링된 데이터 (계시판) 에서  TopN  추출
    m_list  =['apple', 'banana','banana', 'orange','apple','apple', 'banana', 'orange' ]
    count =Counter(m_list)
    print(count)
    print(count. most_common(1)  )

    #r=Counter('abracadabra').most_common(2)
    #print(r)
def test02():
    default_dict = defaultdict(list)
    default_dict['fruits'].append('apple')
    default_dict['fruits'].append('banana')
    print("defaultdict:", default_dict)

def test03():
    d = deque([1, 2, 3, 4, 5])
    d.append(6)
    d.appendleft(0)
    print("deque after append and appendleft:", d)
    d.pop()
    d.popleft()
    print("deque after pop and popleft:", d)

def test04():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(10, 20)
    print("namedtuple Point:", p)
    print("Point fields:", p.x, p.y)

def test05():
    ordered_dict = OrderedDict()
    ordered_dict['banana'] = 3
    ordered_dict['apple'] = 4
    ordered_dict['pear'] = 1
    print("OrderedDict:", ordered_dict)
    for key, value in ordered_dict.items():
        print(key, value)

def test06():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    chain = ChainMap(dict1, dict2)
    print("ChainMap:", chain)
    print("ChainMap['b']:", chain['b'])
    print("ChainMap['c']:", chain['c'])

if __name__ == '__main__':
    test01()