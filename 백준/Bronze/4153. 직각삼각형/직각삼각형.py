# 직각삼각형
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
answer = []

while True:
    num_lst = list(map(int, input().split()))
    #0 0 0입력받으면 입력 끝
    if sum(num_lst) ==0:
        break

    #입력받은 숫자를 오름차순으로 정렬
    num_lst.sort()
    
    #가장 긴 변의 길이를 제곱한 값이 나머지 두 변의 길이를 제곱하여 합한 값과 같다면
    if (num_lst[2]**2) == (num_lst[0]**2)+(num_lst[1]**2):
        answer.append('right')
    else:
        answer.append('wrong')

print(*answer,sep='\n')


## 인덱스가 아닌 min,max로도 가능
# if (max(num_lst)**2) == (min(num_lst)**2)+(num_lst[1]**2):
#     answer.append('ringt')
# else:
#     amswer.append('wrong')
