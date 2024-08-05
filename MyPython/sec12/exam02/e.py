from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<table>
<caption>  mylist  </caption> 
<thead>
<tr>  <th>Name</th>  <th>Age</th>  <th>City</th></tr> 
</thead>
<tbody>
<tr>  <td>John</td>  <td>25</td>  <td>New York</td>
</tr>
</tbody>
<tr>  <td>Alice</td>  <td>30</td>  <td>London</td>
</tr> 
</table>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')  #전체 문서 객체로 리턴
def Test01():
    #1. 테이블의 제목인 thead의  문자열만 출력하자
    thead_text = soup.thead.get_text().strip()  # 리턴되는 문자열의 앞뒤 공백제거
    print(thead_text)
    #2.  tbody의 문자열만 출력하자.
    tbody_text = soup.tbody.get_text().strip()
    print("2. tbody의 문자열:", tbody_text)

def Test02():
    #3.  1,2번으로 추출한 내용을 가지고  caption의 문자열을 파일명으로 지정해서 mylist.txt로 저장하자.
    '''
    temp = soup.caption.get_text().strip()+ '.txt'
    with open(temp, 'w') as f:
        for string in list1:
            f.write(string+',')
        f.write('\n')
        for string in list2:
            f.write(string+',')
    '''
    thead_text = soup.thead.get_text().strip()  # 리턴되는 문자열의 앞뒤 공백제거
    tbody_text = soup.tbody.get_text().strip()
    temp = soup.caption.get_text().strip()+ '.txt'  # caption 태그가 가진 문자열로 파일이름
    with open(temp, 'w') as f:
        f.write(thead_text +"\n" + tbody_text )


if __name__ == '__main__':
    Test02()

