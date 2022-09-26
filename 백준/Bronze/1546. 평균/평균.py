#평균
from sys import stdin

n = int(input())
a = list(map(int,stdin.readline().split()))
aa = []
m = max(a)

for i in a:
    b = i/m*100
    aa.append(b)

result = sum(aa)
print(f'{result/len(aa)}')
