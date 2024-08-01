from bs4 import BeautifulSoup
import urllib.request
import http.client


def Test():
    # python.org 페이지 글을 300자만 출력 해보자.
    f = urllib.request.urlopen('http://www.python.org/')  # 페이지 요청을 바로 해서 다운로드
    print(f.read(300).decode('utf-8'))

def Test01():
    req = urllib.request.Request('http://www.myserver.org/')  # 서버에 요청을 한다.
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print('----------->', e.reason)

def Test02():
    req = urllib.request.Request('http://www.myserver.org/')  # 서버에 요청을 한다.
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('----------->', e)
        print('----------->', e.code)
        print('----------->', e.msg)
        print('----------->', e.hdrs)
        print('----------->', e.fp)

def Test03():
    response = urllib.request.urlopen('http://www.python.org')
    print("response : ", response)  # HTTPResponse
    print("URL  : ", response.geturl())
    print("info  : ", response.info(), type(response.info()))
    headers = response.info()
    print(headers['date'])
    print('')

def Test04():
    # HTTPConnection 객체로 접속
    conn = http.client.HTTPConnection("www.python.org")  # host
    conn.request("GET", "/")
    res = conn.getresponse()
    print(res.msg, type(res.msg))
    for key, value in res.msg.items():
        print(f'{key} ,{value}')


if __name__ == '__main__':
    while True:
        func_name = input("실행할 함수 이름을 입력하세요 (예: Test04, 종료하려면 'exit' 입력): ")
        if func_name == "exit":
            break
        try:
            func = globals()[func_name]
            func()
        except KeyError:
            print(f"'{func_name}'은(는) 존재하지 않는 함수입니다. 다시 입력하세요.")
        except Exception as e:
            print(f"'{func_name}'을(를) 실행하는 동안 오류가 발생했습니다: {e}")
