# 예외가 발생되면 pvm이 예외 종류를 확인하고  확인된 객체를 생성해서 리턴한다.
#  1. 개발자는 예외발생한 위치를 확인하고 try ~ except구문을 작성한다.
#  2. except 구문에서 예외를 처리한다.
if __name__ == '__main__':
   a= 10
   b = 0
   res= 0
   try:
      res = a/b
   except ZeroDivisionError as  zd:
      ####예외를 처리하는 부분
      print(str(zd))
      print(f'{a}  / {b} =  {res}')

   print("=====만줄의 코드 ====")