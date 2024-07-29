#직렬화 , 역직렬화를 구현해 보자
import pickle
from MyPython.sec06.exam.Score import Score as sm
def case01():
    data  =[1,2,3,4,5]
    my = [sm("라라라", 100,100,100), sm("가즈아", 30,60,90)]
    with  open("data.pkl", "wb") as file:
        pickle.dump(data,file)  #직렬화  [객체-> 바이트 스트림] #dump = 저장
        pickle.dump(my, file)

    with  open("data.pkl", "rb") as file:
        load_data  =pickle.load(file) # load = 가져오기
        print(load_data) #역직렬화  [바이트 스트림  -> 객체]
        load_data02 = pickle.load(file)
        print(load_data02)
        for obj in load_data02:
            print(obj)

if __name__ == '__main__':
    case01()

