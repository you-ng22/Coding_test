#과제 안 내신 분..?
#교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

lst = [x for x in range(1, 31)]

for _ in range(28):
    lst.remove(int(input()))
    
print(*lst,sep="\n")