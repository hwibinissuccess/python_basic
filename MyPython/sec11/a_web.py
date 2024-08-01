from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

def test02():
    soup = BeautifulSoup(html_doc, "html.parser")
    ### 1. 제목 가져오기
    print("제목 :",soup.title.string)
    print("=====================")

    ### 2. 첫 p 태그 가져오기
    print("첫 p 태그 :", soup.find('p'))
    print("=====================")

    ### 3. 모든 <a> 태그의 href 속성 추출하기
    a_all = soup.find_all('a')
    for aa in a_all:
        print("href 속성, a 태그들 값 :", aa.get('href'))
    print("=====================")

    ### 4. class가 sister인 모든 <a> 태그의 텍스트 가져오기
    sisters = soup.find_all('a', class_='sister')
    for sister in sisters:
        print(sister.string)
    print("=====================")

    ### 5. ID가 link2인 <a> 태그의 텍스트 출력 -> find() 이용
    res = soup.find('a', id = 'link2')
    print(res.string)
    print("=====================")

    ### 6. 모든 <p>태그의 텍스트 추출
    res = soup.find_all('p')
    for pp in res:
        print(pp.getText())

    ### 7. 특정 속성을 가진 태그 추출하기 - id 태그가 있는 모든 태그를 출력
    all_id = soup.find_all(attrs={'id' : True})
    for tag in all_id:
        print("id 태그 값 :", tag)

    ### 8. 내용 저장 html_doc
    with open("a_web.html", "w", encoding='utf-8') as file :
        file.write(html_doc)

def test03():
    with open("a_web.html", "r", encoding='utf-8') as file:
        html_res = file.read()

    soup = BeautifulSoup(html_res, "html.parser")
    print(f"제목 가져와봥? ->", soup.title.string)

if __name__ == '__main__':
    test03()
