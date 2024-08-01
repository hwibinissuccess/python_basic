'''
홍길동   서울시   02-0000
박길동   부산시   05-0000
정길동   인천시   032-0000

1. 위 내용을 json으로 저장하기 -> name, addr, tel로 키로 지정
 - address_data로 root key값 지정
2. 파일이름을 address.json으로 지정하기
3. 출력을, 이름 : 홍길동, 박길동, 정길동
          전화번호 : ~~~
          주소 : ~~~
'''
import json

if __name__ == '__main__':
    ### 1. address_data에 [{}] 요렇게 data를 저장한다
    address_data = [
        {"name" : "홍길동", "addr" : "서울시", "tel" : "02-0000"},
        {"name" : "박길동", "addr" : "부울시", "tel" : "05-0000"},
        {"name" : "정길동", "addr" : "인울시", "tel" : "032-0000"}
    ]

    ### 2. 데이터 저장 dump ()
    json.dump(address_data, fp=open("address.json", "w"))

    ### 3. 데이터 load()
    data = json.load(fp=open("address.json", "r"))
    print(data)

    ### 4. 데이터 추출 및 출력
    for res in data:
        print(f"이름 : {res['name']}, 전화번호 : {res['tel']}, 주소 : {res['addr']}")

    print("=====================================")

    name = ', '.join(res['name'] for res in data)
    tel = ', '.join(res['tel'] for res in data)
    addr = ', '.join(res['addr'] for res in data)
    print(f"이름 : {name}\n전화번호 : {tel}\n주소 : {addr}")
