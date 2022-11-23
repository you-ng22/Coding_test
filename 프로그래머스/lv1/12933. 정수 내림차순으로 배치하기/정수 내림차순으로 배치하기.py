def solution(n):
    #리스트로 만듦
    lst = list(str(n))
    #내림차순 정렬
    lst.sort(reverse=True)
    
    answer = int(''.join(lst))
    return answer