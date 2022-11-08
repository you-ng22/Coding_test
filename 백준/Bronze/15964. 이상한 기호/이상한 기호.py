#이상한 기호
#A, B가 주어지면 A＠B를 계산하는 프로그램을 만들어주자!

def golbang(a, b):
    answer = (a+b)*(a-b)
    return answer

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(golbang(a, b))