import sys

### A+B - 7
t = int(input())
result = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for idx, value in enumerate(result):
    print(f'Case #{idx+1}: {value}')
