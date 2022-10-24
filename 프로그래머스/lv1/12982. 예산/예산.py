def solution(d, budget):
    answer = 0
    money = 0
    d = sorted(d)
    for i in d:
        money += i
        answer += 1
        if money > budget:
            money -= i
            answer -= 1
            break
    return answer