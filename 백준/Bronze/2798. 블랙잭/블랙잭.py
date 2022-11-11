#블랙잭
#N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

n, m = map(int, input().split())

card = [int(x) for x in input().split()]
sum = 0
answer = 0

#카드 3개를 뽑아야하므로 3중 for문
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum = card[i] + card[j] + card[k]
            #세개의 카드를 합한 수가 m보다 클 경우 continue
            if sum > m:
                continue
            #m보다 작을 경우
            else:
                answer = max(answer, sum)
#세개의 카드를 합한 수가 m보다 작은 값들 중 최댓값 
print(answer)