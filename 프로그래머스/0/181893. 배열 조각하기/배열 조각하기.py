def solution(arr: list[int], query: list[int]):
    answer = arr
    for idx in range(0, len(query)):
        if idx % 2 == 0:
            answer = answer[:query[idx]+1]
        else:
            answer = answer[query[idx]:]
    return answer