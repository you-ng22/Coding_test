#문자열 반복
t = int(input())
for _ in range(t):
    r, s = input().split()

    p = []
    for i in s:
        p.append(i*int(r))

    print(*p, sep='')
