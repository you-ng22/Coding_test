#평균은 넘겠지
c = int(input())

for _ in range(c):
    a = list(map(int, input().split()))
    ave = sum(a[1:])/a[0]
    stu = 0
    for i in a[1:]:
        if ave < i:
            stu += 1
    
    result = (stu/a[0])*100
    print(f'{result:.3f}%')
