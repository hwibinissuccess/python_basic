from bs4 import BeautifulSoup , Comment
markup = "<b><!--Hey, buddy. Want to buy a used parser?--> abcd</b>"
soup = BeautifulSoup(markup, 'html.parser')

# 주석과 문자열을  저장할 리스트 객체
coment_all =[]
text_all =[]

for  element in   soup.b.children:
     if isinstance(element,Comment):  #  객체의 타입 유무확인 메소드
        coment_all.append((element))
     elif  isinstance(element, str):
         text_all.append(element.strip())

print(coment_all )
print(text_all)

for string in soup.strings:
    print(repr(string))

