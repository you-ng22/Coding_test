s = input()
d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
hap = 0

for i in range(len(s)):
    for j in d:
        if s[i] in j:
            hap += d.index(j)+3

print(hap)