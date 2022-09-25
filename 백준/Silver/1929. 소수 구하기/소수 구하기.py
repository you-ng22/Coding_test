#소수 구하기
m, n = map(int, input().split())
# l = []

# for i in range(m, n+1):
#     count = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             count += 1
#     if count == 2:
#         l.append(i)
# print(*l, sep="\n")


for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        print(i)