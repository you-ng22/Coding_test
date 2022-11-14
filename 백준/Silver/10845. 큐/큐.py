#큐
#정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
from sys import stdin

n = int(stdin.readline())
queue = []
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue :
            print(queue.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
