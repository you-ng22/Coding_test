import sys

###빠른 A+B
t = int(sys.stdin.readline())
c = []
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    c.append(a+b)

for j in c:
    print(j)