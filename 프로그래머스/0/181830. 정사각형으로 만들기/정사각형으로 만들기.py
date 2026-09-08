def solution(arr):
    answer = [[]]
    length_x = len(arr)
    length_y = len(arr[0])
    length = max(length_x, length_y)
    for i in range(length):
        if i != length-1: answer.append([])
        for j in range(length):
            if j < length_y and i < length_x:
                answer[i].append(arr[i][j])
            else: 
                answer[i].append(0)
    return answer