#검증수
#각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.
#첫째 줄에 검증수를 출력한다.

def six_num(five_num):
    five_num = [pow(num,2) for num in five_num]
    answer = sum(five_num) % 10
    return answer

if __name__ == '__main__':
    five_num = list(map(int,input().split()))
    print(six_num(five_num))