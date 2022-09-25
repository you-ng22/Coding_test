# x보다 작은 수 
from sys import stdin

n, x = map(int, input().split())
a = stdin.readline().split()
list = []

for i in a:
    if int(i) < x:
        list.append(i)

print(*list)