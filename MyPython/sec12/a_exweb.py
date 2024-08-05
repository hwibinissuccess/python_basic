from bs4 import BeautifulSoup
# 요소의 속성 값 찾는 방법
html_doc = """
<html>
<body>
<h1>Links</h1>
<ul>
    <li><a href="https://www.example.com">Example 1</a></li>
     <li> <a href="https://www.google.com">Example 2</a></li>
     <li> <a href="https://www.openai.com">Example 3</a></li>
</ul>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
def Test01():
    links = [a['href'] for a in soup.select('body ul li a')]
    for link in links:
        print(link)
    '''
    요소 복사  : <a href="https://www.example.com">Example 1</a> 
    body > ul > li:nth-child(1) > a     
    '''
    print('=======================================')
    selected_tag = soup.select('body > ul > li:nth-child(1) > a')
    print(selected_tag)
    for res  in selected_tag:
        print(res)
        print(res.get_text())
        print(res['href'])

    print('=======================================')
    selected_tag = soup.select('body > ul > li ')
    print(selected_tag)
    for res in selected_tag:
        print(res)
        print(res.get_text())
        if res.a :
            print(res.a['href'])

def Test02():
    ########################## find_all()
    link_res  =  [a['href']  for a  in soup.find_all('a')]
    for link  in link_res:
        print(link)

if __name__ == '__main__':
    Test01()





