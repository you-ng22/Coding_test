#음계
#연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.

def scale(x):
    # x = list(map(int, input().split()))
    if x == [i for i in range(1,9)]:
        return 'ascending'
    elif x == [j for j in range(8,0,-1)]:
        return 'descending'
    else:
        return 'mixed'

if __name__ == '__main__':
    x = list(map(int, input().split()))
    print(scale(x))