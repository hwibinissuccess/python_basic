def test():
    #for and dict
    m_dict = {'x': 1, 'y': 2, 'z': 3 }
    print(m_dict.items() )

    print("=======================================")
    for key in m_dict:
        print (key, '+', m_dict[key])

    print("=======================================")
    for key,value in m_dict.items():
        print (key, '+', value)

def test01():
    m_dict = {'x': 1, 'y': 2, 'z': 3}
    #1.값 접근
    print(f'{m_dict['x']}')
    print(f'{m_dict['y']}')
    print(f'{m_dict['z']}')
   #2.값 추가
    m_dict['a'] =100
    print(m_dict)
   #3.값 수정
    m_dict['a'] = 9999
    print(m_dict)
    #4.항목 삭제
    del m_dict["a"]
    print(m_dict)

if __name__ == '__main__':
    test01()

