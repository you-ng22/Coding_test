def solution(arr, divisor):
    answer = []
    # 나머지가 0인 값을 answer리스트에 추가
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    # answer이 빈 리스트라면 -1을 리스트에 추가
    if len(answer) == 0:
        answer.append(-1)
    # answer 리스트를 오름차순으로 정렬
    answer.sort()    
    return answer