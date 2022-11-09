def solution(strings, n):
    answer = []
    lst = []
    for string in strings:
        #n부터 정렬을 위해 첫글자로 인덱스n이 오도록
        x = string[n] + string
        lst.append(x)
    lst.sort()
    
    for j in lst:
        #더해진 인덱스n 문자열 빼고 출력하기 위해 인덱싱
        answer.append(j[1:])
    return answer