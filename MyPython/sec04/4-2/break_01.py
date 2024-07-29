def Test():# 1~ 9까지 출력하되  숫자가 5보다 크면 break 하자
    for i in range(1,10):
                if i > 5:
                        break
                print("%5d"%i,end="")
    else:
        print("~ else~ ")

    print(" outter = %5d"%i,end="")


def Test01():
    for i in range(1, 10):
        if i > 3:
            continue  #반복을 계속하자.
        print("%5d" % i, end="")
        print("//")

    print(" outter = %5d" % i, end="")

def Test02():
    for i in range(1, 10):
        if i > 5:
            print(f" \n {i} > 5 ~~~" , end= " ")
            continue
        print("%5d" % i, end="")
    else:
        print("=======else=========")

    print(" outter = %5d" % i, end="")

if __name__ == '__main__':
    #print(Test01())  # return이 없는 함수를 호출해서 출력할 때 None
    Test02()