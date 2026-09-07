def solution(arr: list[int]):
    answer = arr
    length = 1024
    length_arr = len(arr)
    while True:
        if length // length_arr == 1:
            break
        else:
            length //= 2
    for _ in range(len(arr), length):
        answer.append(0)
    return answer