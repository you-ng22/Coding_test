def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        #배열을 자른후 새로운 배열 만들어줌
        new_arr = array[commands[i][0]-1:commands[i][1]]
        #오름차순 정렬
        new_arr.sort()
        
        #정렬된 배열에서 인덱스로 k번째 수 찾음
        answer.append(new_arr[commands[i][2]-1])

    return answer