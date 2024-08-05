from bs4 import BeautifulSoup
#1. olview.html 파일을 로드해서 soup 객체를 생성한다.
with open("../myhtml/olview.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
#print(soup.prettify())
#print(soup)
def Test01():
    #2. 모든  <o1> 태그를 추출하자.
    ol_tag  =  soup.find_all('ol')

    for ol in ol_tag:
        print(ol)

def Test02():
    #3.  <o1> 태그 중  속성이   type "a" 만 추출 해보자.
    res = soup.find_all('ol', {'type':'a'})
    for  ol in res:
        print(ol)

def Test03():
    #4.  <o1> 태그 중  속성이   type "A" 의 li 의 값만 추출 해보자.
    res02 = soup.find_all('ol', {'type':'A'})
    li_texts  = [li.get_text()  for  ol in  res02
                                      for  li in ol.find_all( 'li') ]
    for  text in li_texts:
        print(text)

if __name__ == '__main__':
    Test03()



