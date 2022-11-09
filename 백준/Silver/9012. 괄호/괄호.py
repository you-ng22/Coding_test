#괄호
#입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

n = int(input())
answer = []

for i in range(n):
    word = input()
    strings = list(word)
    sum = 0

    for string in strings:
        if string == '(':
            sum += 1
        elif string == ')':
            sum -= 1
        if sum < 0:
            answer.append('NO')
            break
    if sum > 0:
        answer.append('NO')
    elif sum == 0:
        answer.append('YES')

print(*answer,sep='\n')