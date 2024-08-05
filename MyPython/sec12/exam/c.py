from bs4 import BeautifulSoup , Comment , NavigableString
markup = "<b><!--Hey, buddy. Want to buy a used parser?--> abcd</b>"
soup = BeautifulSoup(markup, 'html.parser')

# 주석과 문자열을  저장할 리스트 객체
coment_all =[]
text_all =[]

def Test01() :
    print(help(soup.recursiveChildGenerator ))  # 모든 자식 요소를 재귀적으로 순회 하면서  리턴 해주는 함수
    print(soup.recursiveChildGenerator())

    print("===========================================")
    for  element in   soup.recursiveChildGenerator():
         if isinstance(element,Comment):
            coment_all.append((element))
         elif  isinstance(element, str):
             text_all.append(element.strip())
    print(coment_all )
    print(text_all)

def Test02():
    for  element in   soup.descendants:
         if isinstance(element,Comment):
            coment_all.append((element))
         elif  isinstance(element, str) and not element.name:
             text_all.append(element.strip())
    print(coment_all )
    print(text_all)

def Test03():
    #b_exam.html의 내용을 적용해 보자.  => ['html', '', '', '', '', 'Title', '', '']
    with open("b_exam.html",'r' , encoding='utf-8') as file:
        content  = file.read()
    soup  = BeautifulSoup(content, "html.parser")
    for  element in  soup.descendants:
         if isinstance(element,Comment):
            coment_all.append((element))
         elif  isinstance(element, str) and not element.name:
             text_all.append(element.strip())
    print(coment_all )
    print(text_all)
def Test04():
    #b_exam.html의 내용을 적용해 보자.  => ['html', '', '', '', '', 'Title', '', '']
    coment_all =[]
    text_all=[]
    with open("b_exam.html",'r' , encoding='utf-8') as file:
        content  = file.read()
    # 제외할 태그를 지정
    soup  = BeautifulSoup(content, "html.parser")
    body = soup.body   #바디 태그
    for element in body.descendants:
        if isinstance(element, Comment):
            coment_all.append(element)
        elif isinstance(element, str) and element.strip():
            text_all.append(element.strip())

    print(coment_all )
    print(text_all)
if __name__ == '__main__':
    Test04()

