def solution(arr: list[int]):
    answer = []
    answer.append(arr[0])
    for num in arr:
        if answer[-1] != num:
            answer.append(num)

    return answer