import os

def count_keyword_occurrences(filename, keyword):
    with open(filename, "rb") as file:
        lines = file.readlines()
        count = 0
        for i, line in enumerate(lines, 1):
            line = line.decode('utf-8')
            if keyword in line:
                print(f"키워드 '{keyword}'가 {i}번째 줄에 등장합니다.")
                count += 1
        print(f"키워드 '{keyword}' 총 등장 횟수: {count}")

if __name__ == '__main__':
    keyword = input("찾고자 하는 키워드: ")
    count_keyword_occurrences("log.txt", keyword)
