from bs4 import BeautifulSoup
#1. olview.html 파일을 로드해서 soup 객체를 생성한다.
with open("../myhtml/olview02.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
#print(soup.prettify())
#for tag in soup.select('*'):
#css_classes : {'b1', 'a1'}
#clss_id : {'e1', 'c1', 'd1'}

def Test01():
    ###################select()
    #1.  id중에 e1인 태그를 찾아서   값만 출력 해보자.  select_one()
    id_res  = soup.select_one('#e1')
    if id_res:
        print(id_res.get_text())

def Test02():
    #2. class중에 a1인 태그를 찾아서 값만 출력 해보자. select()
    class_res  = soup.select('.a1')
    for tag  in class_res:
        print(tag.get_text())
def Test03():
    ######################## find_all()
    #1.  id중에 e1인 태그를 찾아서   값만 출력 해보자. find()
    id_res  = soup.find(id='e1')
    if id_res:
        print(id_res.get_text())

def Test04():
    #2. class중에 a1인 태그를 찾아서 값만 출력 해보자. find_all()
    class_res  = soup.find_all(class_='a1')
    for tag  in class_res:
        print(tag.get_text())


if __name__ == '__main__':
     Test04()
