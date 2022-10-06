# 단어공부
s = list(input().upper())
m = [s.count(x) for x in set(s)]
n = max(m)

if m.count(n) > 1:
    print('?')
else:
    for i in set(s):
        if n == s.count(i):
            print(i)