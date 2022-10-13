# 상수

a = list(map(int, input().split()))
l = []

for i in a:
    s = int(str(i)[::-1])
    l.append(s)

print(max(l))