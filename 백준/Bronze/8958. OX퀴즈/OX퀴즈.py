# O X 퀴즈
from sys import stdin

n = int(input())
for _ in range(n):
    a = list(input())
    count = 0
    add_value = 1
    for i in a:
        if i == 'O':
            count += add_value
            add_value += 1
        else:
            add_value = 1
    print(count)