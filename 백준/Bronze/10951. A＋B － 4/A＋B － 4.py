import sys
sum_list = []

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())        
    except:
        break
    sum_list.append(a+b)

print(*sum_list, sep="\n")