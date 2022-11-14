#수 찾기
#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

n = int(input())
n_num = set(map(int, input().split()))

m = int(input())
m_num = list(map(int, input().split()))

answer = []
for i in m_num:
    if i in n_num:
        answer.append('1')
    else:
        answer.append('0')

print(*answer,sep='\n')