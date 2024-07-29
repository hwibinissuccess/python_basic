
#enumerate()함수 미사용 한 경우
fruit  = ['apple','watermelon','peach','pear']
for i in range(len(fruit)):  # range()로  fruit길이만큼 숫치로 만들어서 i로 리턴
   print(i+100, fruit[i])  # 100  apple


print('--------------------------')
#enumerate()함수 사용 한 경우
for i, res in enumerate(fruit,100):
       print(i,res)

#결과를 파일로 저장해보자.
with open('fortest.txt', 'w') as file:
    for i, res in enumerate(fruit,100):
           file.write(f"{i},{res} \n")

with open('fortest.txt', 'r') as file:
    print(file.read())