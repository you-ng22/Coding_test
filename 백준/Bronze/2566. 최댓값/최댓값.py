#최댓값
#9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
arr = [list(map(int, input().split())) for _ in range(9)]

max = arr[0][0]
x, y = 0,0
for i in range(0, 9):
    for j in range(0, 9):
        if arr[i][j] > max:
            max = arr[i][j]
            x = i
            y = j
 
print(max)
print(x+1, y+1)
