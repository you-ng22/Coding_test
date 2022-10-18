#그룹 단어 체커
n = int(input())

for _ in range(n):
    s = input()
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            pass
        elif s[i] in s[i+1:]:
            n -= 1
            break
print(n)
    
    # 인덱스
    # 첫글자와 다음글자 같으면 상관없
    # 다르면 앞에 나왔던 글자 나오면 x
