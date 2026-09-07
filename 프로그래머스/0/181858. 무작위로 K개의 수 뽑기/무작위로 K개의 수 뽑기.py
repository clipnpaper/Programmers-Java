def solution(arr: list[int], k: int):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer) >= k:
            break
    for _ in range(len(answer), k):
        answer.append(-1)
    return answer