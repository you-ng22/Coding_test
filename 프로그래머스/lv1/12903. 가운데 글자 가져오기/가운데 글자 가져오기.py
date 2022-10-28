def solution(s):
    answer = ''
    #글자수 홀수
    if len(s)%2:
        answer = s[len(s)//2]
    #글자수 짝수
    else:
        answer = s[(len(s)//2)-1]+s[len(s)//2]
        
    return answer