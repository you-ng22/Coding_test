#a+b - 5 / 0 입력하면 break
import sys
sum_list = []

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    sum_list.append(a+b)

print(*sum_list, sep='\n')
