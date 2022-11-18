def solution(arr):
    answer = []
    #처음숫자는 결과값에 append
    answer.append(arr[0])
    for i in range(1, len(arr)):
        #두번째 숫자부터 시작
        #지정된 숫자와 그 전 숫자가 다르다면
        if arr[i] != arr[i-1]:
            #결과값이 지정된 숫자 append
            answer.append(arr[i])
    return answer