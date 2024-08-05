from bs4 import BeautifulSoup
markup = "<b>python !!! <!-- Hey, buddy. Want to buy a used parser? --> abcd</b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment)
print(type(comment))
# <class 'bs4.element.Comment'>

comment = soup.b.text  #str
print(comment)
print(type(comment))

comment = soup.get_text() # str
print(comment)
print(type(comment))
'''
string  : 단일 텍스트 노드 단, 자식노드가 있으면 NoneType를 리턴  
text : 요소 내 모든 텍스트를 공백 포함 후 하나의 문자열로 리턴  , 자식 노드 텍스트 포함  
get_text() : 요소 내 모든 텍스트를 공백 포함 후 하나의 문자열로 리턴 , 출력서식 제어
get_text(separator='', strip=False)   
'''
print( help (soup.get_text) )

print("<===============================>")
b_tag  = soup.find('b')
print(  b_tag.get_text(separator='|', strip=True))






