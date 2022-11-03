def solution(a, b):
    #a가 b보다 작거나 같을 때
    if a <= b:
        return sum(range(a, b+1))
    #b가 a보다 작을 때
    else:
        return sum(range(b, a+1))