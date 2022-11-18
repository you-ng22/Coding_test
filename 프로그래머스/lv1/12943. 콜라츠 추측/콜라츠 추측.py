def solution(num):
    answer = 0
    while True:
        #입력받은 수가 1일경우
        if num == 1:
            return answer
        #횟수가 500이 되면 -1
        if answer == 500:
            return -1
        #짝수 일경우 2로 나눈값을 변수에 저장
        if num % 2 == 0:
            num = num / 2
        #홀수 일경우 3을 곱하고 1을 더함
        elif num % 2 == 1: 
            num = num * 3 + 1
         #작업을 마치고 횟수에 1 더함
        answer += 1 

    return answer