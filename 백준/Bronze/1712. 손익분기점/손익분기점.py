# 손익분기점
a, b, c = map(int, input().split())

if c-b <= 0:
    print(-1)
elif c-b>0:
    print(int(a//(c-b)+1))