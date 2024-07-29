# 10, -1 , 0

# 숫자 입력받아서  0보다 크면  "Positive number" , 숫자 출력하고,  0이랑 같으면  Zero, 숫자 출력 하고
#나머지는  "Negative number" , 숫자 출력 하자.  
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
    print(num)
elif num == 0:
    print("Zero")
    print(num)
else:
    print("Negative number")
    print(num)
