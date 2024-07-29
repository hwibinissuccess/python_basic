#피클링 작업을 해보자  byte, char, object
# 직렬화 pickle = 바이트 스트림으로 변환   ,   역직렬화 un-pickle  바이트스트림 -> 객체
# 확장자  :  .pkl     / 가중   시험  = (중간고사*0.4) +  (기말고사*0.6)  / 2
#   학습  : 오류값이 가장 작을 때 까지  최적화 함수를 통해  가중치를 업데이트(step)하는 과정
#   최적화함수  -> 활성화함수  -> 로스함수
# 노드,엣지,텐서,텐서플로우  /  이진분류, 다중분류, 다중클래스 분류
try:
    import cPickle  # 임포트 cPickle  -> 객체를 피클링 하는 모듈 / dump(), load()
    pickle = cPickle #pickle로 대입한다 , 대입시 cPickle이 없다면 프로그램은 중단이 되기 때문에 except로 이동
except:
    import pickle  #임포트 pickle

book ={'java':30000,'jsp':35000,'oracle':40000, 'python': 20000}
list =["abcd",90,90.8]
Tuple =(book, list)  # 객체들을  Tuple로 묶어서
print(Tuple)  #출력해 본다.

f= open('ptest.pkl','wb' )  # 바이트로 출력하는 파일의 속성을 지정한다.
pickle.dump(Tuple,f) #파일에 객체를 저장
f.close()

f = open("ptest.pkl","rb")# 바이트로 읽어들이는  파일의 속성을 지정한다.
res01, res02= pickle.load(f) # 파일의 객체를 로드한다.
print("res ======>" , res01)
print("res02=====>", res02)

