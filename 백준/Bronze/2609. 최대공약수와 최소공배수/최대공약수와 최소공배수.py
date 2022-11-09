#최대공약수와 최소공배수
#두 개의 자연수를 입력받아 최대공약수와 최소공배수를 출력하는 프로그램을 작성하시오.

def solution(n, m):
    gcdlcm = []
    #최대공약수
    for i in range(min(n, m),0,-1):
        if n%i == 0 and m%i == 0:
            gcdlcm.append(i)
            break
    #최소공배수
    for j in range(max(n, m),(n*m)+1):
        if j%n == 0 and j%m == 0:
            gcdlcm.append(j)
            break
    return gcdlcm

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(*solution(n,m),sep='\n')