#그대로 출력하기
#입력 받은 대로 출력하는 프로그램을 작성하시오.

while True:
    try:
        print(input())
    #EOFError_입력이 끝남(End Of File)
    except EOFError:
        break