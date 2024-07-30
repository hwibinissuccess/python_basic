#https://docs.python.org/3/tutorial/errors.html
import sys
import chardet

def test():
    try:
        f = open('myfile.txt')  #FileNotFoundError
        s = f.readline()
        i = int(s.strip())
    except FileNotFoundError  as  e :
        print("0). FileNotFoundError:", e)
    except OSError as err:
        print("1). OS error:", err)
    except ValueError:
        print("2). Could not convert data to an integer.")
    except Exception as err:
        print(f"3). Unexpected {err=}, {type(err)=}")
        #raise
def test02():
    for arg in sys.argv[1:]:  # 실행시 값을 인수로 전달
        try:
            f = open(arg, 'r',encoding='utf-8', errors='ignore') #디코딩 오류 무시
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()

def test03():  ########번외 편  ###########  echo "12345" > a.txt   / cat a.txt
    ####파이썬에서 인코딩이 불안한 경우 'chardet'를 이용해서 인코딩을 감지 해서 적용 한다.
    for arg in sys.argv[1:]:  # 실행시 값을 인수로 전달
        try:
            with  open( arg, 'rb') as f:
                row_data  = f.read()  # 전체를 읽어서 리턴  byte
                res  = chardet.detect(row_data)
                print(res)  # {'encoding': 'EUC-JP', 'confidence': 0.99}
                encoding  = res['encoding']

            f = open(arg, 'r', encoding=encoding)
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
        finally:
            f.close()


def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

#if __name__ == '__main__':
#    test03()