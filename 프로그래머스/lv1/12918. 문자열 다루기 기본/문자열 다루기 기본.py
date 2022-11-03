def solution(s):
    # 문자열 길이가 4, 6인지 확인
    if len(s) == 4 or len(s) == 6:
        # isdigit()메서드로 숫자로만 이루어져있는지 확인 
        if s.isdigit() == True:
            return True
        # 문자열이 들어있다면 False
        else:
            return False
    #문자열 길이가 4, 6이 아니라면 Flase
    else:
        return False