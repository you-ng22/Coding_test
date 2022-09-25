#더하기 사이클

n = int(input())
cyc = 0
sum = n

while True:
    a = n//10
    b = n%10
    c = (a+b)%10
    n = (b*10)+c
    cyc += 1
    if n == sum:
        break
print(cyc)