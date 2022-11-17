#요세푸스 문제
#N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

def josephus(n, k):
    n_lst = list(range(1,n+1))
    answer = []
    idx = 0
    for i in range(n):
        idx += k-1
        if idx >= len(n_lst):
            idx = idx%len(n_lst)
        
        answer.append(str(n_lst.pop(idx)))
        
    return answer

if __name__ == '__main__':
    n, k = map(int, input().split())
    
    print('<',', '.join(josephus(n, k)),'>',sep='')


# n, k = map(int, input().split())
# n_lst = list(range(1,n+1))
# answer = []
# idx = 0

# for i in range(n):
#     idx += k-1
#     if idx >= len(n_lst):
#         idx = idx%len(n_lst)
    
#     answer.append(str(n_lst.pop(idx)))

# print('<',', '.join(answer),'>',sep='')

