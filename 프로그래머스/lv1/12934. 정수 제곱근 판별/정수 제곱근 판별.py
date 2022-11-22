def solution(n):
    #n의 1/2 제곱은 n의 제곱근
    x = n ** (1/2)
    #x를 1로 나눈 나머지가 0일 때 x+1의 제곱을 return 하도록
    if x % 1 == 0:
        return (x + 1) ** 2
    #if문이 실행되지 않았을 경우엔 n의 제곱근이 정수가 아님
    return -1