#이하아 계수 1
#자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

n,k = map(int, input().split())
x = n - k
n_fac = 1
k_fac = 1
x_fac = 1

# n! k! (n-k)! 을 구함
for i in range(n, 1, -1):
    n_fac = n_fac * i

for j in range(k, 1, -1):
    k_fac = k_fac * j

for k in range(x, 1, -1):
    x_fac = x_fac * k

print(int(n_fac/(k_fac*x_fac)))