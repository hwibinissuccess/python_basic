
def for_test01():
   for  res in [1,2,3,4]:
	   print(f'{res}', end=' ')

def for_test02():
   for  res in (1,2,3,4):
	   print(f'{res}', end=' ')

def  for_test03():
	print(range(10) , list(range(10))  , list(range(0,100,2))  )
	for  x  in  range(10):
		print(f'{x}', end=' ')


def for_test05():  # 100포함입니다.
	#0~ 100 까지 정수 , 5의 배수만 출력 하고 싶다.  range(), for
	for  x  in  range(0,101,5):
		print(f'{x}', end=' ')

	print('\n ================================== \n')
    #100~ 0 까지 정수를 역순으로 출력 하고 싶다.
	res = list(range(100, -1, -1))
	for  x  in res :
		print(f'{x}', end=' ')

def  for_test04():
	fruit  = ['apple','watermelon','peach','pear']
	if "apple" in fruit or len(fruit) > 5 :
		for m_f in fruit:
			print(m_f)

if __name__ == '__main__':
    for_test04()




