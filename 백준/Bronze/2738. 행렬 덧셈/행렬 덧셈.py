#행렬 덧셈
#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]

for i in a:
    print(*i)