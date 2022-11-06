#학점계산
#어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.

c = input()

if c == 'A+':
    print(4.3)
elif c == 'A0':
    print(4.0)
elif c == 'A-':
    print(3.7)
elif c == 'B+':
    print(3.3)
elif c == 'B0':
    print(3.0)
elif c == 'B-':
    print(2.7)
elif c == 'C+':
    print(2.3)
elif c == 'C0':
    print(2.0)
elif c == 'C-':
    print(1.7)
elif c == 'D+':
    print(1.3)
elif c == 'D0':
    print(1.0)
elif c == 'D-':
    print(0.7)
else:
    print(0.0)