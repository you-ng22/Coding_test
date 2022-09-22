import sys

### A+B - 8
t = int(input())
# result = []

for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    # result.append(a+b)
    # for idx, value in enumerate(result):
    print(f'Case #{i}: {a} + {b} = {a+b}')