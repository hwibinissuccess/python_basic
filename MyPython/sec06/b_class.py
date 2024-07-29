from sec06.exam.Score import Score

if __name__ == '__main__':
    s1 = Score("홍길동", 90, 80, 70)
    s2 = Score("정길동", 50, 60, 70)
    s3 = Score("이길동", 100, 100, 100)

    print(s1)
    print(s2)
    print(s3)

    print("===== 전체 내용을 출력  ======")
    print(f'{s1.name:<5} {s1.kor:5d}  {s1.eng:5d} {s1.mat:5d}  {s1.getTot()}  {s1.getAvg():5.1f}   {s1.getGrade()}')
    print(f'{s2.name:<5} {s2.kor:5d}  {s2.eng:5d} {s2.mat:5d}  {s2.getTot()}  {s2.getAvg():5.1f}   {s2.getGrade()}')
    print(f'{s3.name:<5} {s3.kor:5d}  {s3.eng:5d} {s3.mat:5d}  {s3.getTot()}  {s3.getAvg():5.1f}   {s3.getGrade()}')