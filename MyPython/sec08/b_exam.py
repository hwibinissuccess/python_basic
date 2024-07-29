'''
1. 현재 파이썬에서 기본 인코딩을 확인하려면 sys 모듈의 메소드를 사용한다.
     'getdefaultencoding'
     stden, stdout, stderr -> encoding 속성을 통해 확인
2. 인코딩 목록을 확읺 ㅏ려면  encodings
'''

import sys
import encodings

def Test01():
    print(f'1. 기본 인코딩 : {sys.getdefaultencoding()}')
    print(f'2. 표준 입력 스트림 인코딩 : {sys.stdin.encoding}')
    print(f'3. 표준 출력 스트림 인코딩 : {sys.stdout.encoding}')
    print(f'4. 표준 오류 슽느림 인코딩 : {sys.stderr.encoding}')

def Test02():
    # encodings 모듈에서 사용가능한 인코딩 목록을 가져오기 : 인코딩 모듈이 가진 인코딩 별칭의 값들을 출력해보자
    res = set(encodings.aliases.aliases.values())
    print(res)