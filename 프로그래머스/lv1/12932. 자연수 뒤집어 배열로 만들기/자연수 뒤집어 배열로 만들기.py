def solution(n):
    #각 자리수를 리스트 형식으로 만듦
    answer = list(map(int,str(n)))
    #리스트를 뒤집는다. 
    #인덱스 사용가능 [::-1]
    answer.reverse()

    return answer