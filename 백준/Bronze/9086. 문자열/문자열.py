#문자열
#문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

test_num = int(input())

for _ in range(test_num):
    word = str(input())
    print(word[0],word[-1],sep='')