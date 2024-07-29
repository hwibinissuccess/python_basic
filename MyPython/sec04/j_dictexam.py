from  datetime import datetime, date
mydoc = {
    '_id': ("5099803df3f4948bd2f98391"),
    'name': {'first': "Alan", 'last': "Turing"},
    'birth': datetime.strptime('Jun 23, 1912', '%b %d, %Y').date(),
    'death': datetime.strptime('Jun 07, 1954', '%b %d, %Y').date(),
    'contribs': ["Turing machine", "Turing test", "Turingery"],
    'views': int(1250000)
}
def  case02(): #value중에 date 객체만 추출해서 출력하고 싶다.
    #날짜 값만 추출해서 리턴하자.
    my_dates ={}
    for key, value  in mydoc.items():
        if isinstance(value, date) :
            my_dates[key]=value
    return my_dates

#def case03(): #value중에 str 객체만 추출해서 출력하고 싶다.

def case01():
    for key,value in mydoc.items():
        print (f'{key} + {value}')
    print('------------------------------------')
    print(mydoc['contribs'])
    print('------------------------------------')
    print(mydoc['name']['last'])
if __name__ == '__main__':
    res  = case02()
    for k, v   in res.items():
        print(f"{k.capitalize() } Date : {v}")