from bs4 import BeautifulSoup

with open("my.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#요소를 root 로 찾아가기
print(soup.html.body.p)
print(soup.html.body.a['class'])
print(soup.html.body.a['href'])
print(soup.html.body.a['id'])
print(soup.html.body.p.text)
print("1111=======================")

print( help(soup.find))
print(soup.find('p').text)
res  = soup.findAll('a')
for  m_res  in res:
    print(m_res['href'])

print("2222=======================")
res  = soup.findAll('a')
for  m_res  in res:
    print(f" {m_res.text} \t {m_res['href'] }")

print('--------------------------')
for string in soup.strings:
    print(repr(string))