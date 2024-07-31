import json

def Test01():
    data = [{'a' : 'A', 'b' : (2,4), 'c' : 3.0}] # list
    print('data : ', data, 'repr(data) : ', repr(data), str(data))
    print(type(data), type(repr(data))) # 둘의 타입은 다름, 전자는 list, 후자는 class
    print("====================================")
    data_string = json.dumps(data) # Serialize obj to a JSON formatted str. 파이썬 데이터를 json형식으로 변환 후 문자열로 리턴
    print('json : ', data_string, type(data_string))
    # json은 싱글퍼터가 아니라 더블퍼터로 되어 있고, 토플이 list로 되어 나옴

def Test02(): # 리스트(가변), 튜플(불변)!
    data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]  # list
    data_string = json.dumps(data, indent=4, sort_keys=True) # 인코딩
    print("Encoded : ", data_string)
    #repr(data_string)
    decoded = json.loads(data_string) # 디코딩
    print("decoded : ", decoded, type(decoded)) # type 확인

def Test03():
    '''
    Deserialize ``s`` (a ``str``, ``bytes``or``bytearray`` instance
    containing a JSON document) to a Python objct.
    파이썬에서 json문서를 객체로 역직렬화를 하려면 str, bytes, bytearry => 파이썬 객체로 변환
    '''
    obj_json_str = '{"str" : [42.2,1,2,3,4,5], "str01" : 42, "str02" : 100}'
    obj_json_bytes = b'{"str" : [42.2,1,2,3,4,5], "str01" : 42, "str02" : 100}'
    obj_json_bytearray = bytearray(b'{"str" : [42.2,1,2,3,4,5], "str01" : 42, "str02" : 100}')# str
    obj1 = json.loads(obj_json_str) # 문자열을 읽어서 -> json으로 리턴 -> obj 타입을 dict로
    obj2 = json.loads(obj_json_bytes)
    obj3 = json.loads(obj_json_bytearray)
    print(obj1, type(obj1))
    print(obj2, type(obj2))
    print(obj3, type(obj3))
    print(json.dumps(obj1, indent=4, sort_keys=True))
    print(json.dumps(obj2, indent=4, sort_keys=True))
    print(json.dumps(obj3, indent=4, sort_keys=True))

def Test04():
    obj_json = {"str" : [42,2], "str01" : 42, "str03" : [42.2,1,2,3,4,5], "str02" : '대한민국'}
    file = "data.json"
    json.dump(obj_json, fp=open(file,'w'), indent=4, sort_keys=True)

    # 파일에서 읽어서 화면 출력하기
    file = open("data.json", 'r')
    result = json.load(fp=file)
    print(result) ## 강사가 그냥 넘어감 보충해야함

if __name__ == '__main__':
    Test03()