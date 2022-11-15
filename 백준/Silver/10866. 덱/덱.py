#덱
#정수를 저장하는 덱를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
from sys import stdin
from collections import deque

n = int(stdin.readline())
deq = deque()
for _ in range(n):
    command = stdin.readline().split()
    if command[0] == 'push_front':
        deq.appendleft(command[1])
    elif command[0] == 'push_back':
        deq.append(command[1])
    elif command[0] == 'pop_front':
        if deq :
            print(deq.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deq :
            print(deq.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif command[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
