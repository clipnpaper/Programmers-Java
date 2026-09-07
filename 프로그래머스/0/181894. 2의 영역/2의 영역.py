def solution(arr: list[int]):
    answer = []
    start_index = -1
    end_index = -1
    for index in range(0, len(arr)):
        if arr[index] == 2:
            start_index = index
            break
    for index in range(len(arr)-1, -1, -1):
        if arr[index] == 2:
            end_index = index
            break
    if start_index == -1: return [-1]
    answer = arr[start_index:end_index+1]
    return answer