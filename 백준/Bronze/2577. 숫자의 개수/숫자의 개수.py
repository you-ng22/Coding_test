#숫자의 개수
#세 개의 자연수 A,B,C가 주어질 때 A x B x C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

def count_num(a, b, c):
    lst = []
    answer = list(str(a*b*c))
    for i in range(10):
        lst.append(answer.count(str(i)))
    return lst

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(*count_num(a, b, c),sep='\n')