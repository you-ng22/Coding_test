#나머지
n = [int(input()) for i in range(10)]
h = []

for i in n:
    l = i%42
    h.append(l)

hh = set(h)
print(len(hh))