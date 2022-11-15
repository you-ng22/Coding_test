#카드2
#N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
from collections import deque

n = int(input())
n_lst = deque(range(1,n+1))

while len(n_lst) > 1:
    #제일 앞 숫자 제거
    n_lst.popleft()
    #2번째였던 숫자를 제거하면서 변수에 저장
    num = n_lst.popleft()
    #제거했던 숫자 append
    n_lst.append(num)
    
print(*n_lst)

