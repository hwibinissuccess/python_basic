from bs4 import BeautifulSoup
#1. olview02.html 파일을 로드해서 soup 객체를 생성한다.
with open("../myhtml/olview02.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
#print(soup.prettify())

css_classes  = set()  #클래스들을 담을  빈 객체 생성
clss_id  = set()   #id들을 담을 빈 객체 생성

#모든 태그를 탐색 find_all(True)
for tag in soup.find_all(True):
# 클래스 속성이 있는 경우 값을 추출해서 저장    'class' in  tag.attrs:
  if  'class' in  tag.attrs:
      css_classes.update(tag['class'])
# id속성이 있는 경우  값을 추출해서 저장
  if   'id' in  tag.attrs:
      clss_id.add(tag['id'])

print( " css_classes :"  ,css_classes  )
print("clss_id :" , clss_id )

