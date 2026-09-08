def solution(n: int):
    answer = [[]]
    for i in range(n):
        if i != n-1: answer.append([])
        for j in range(n):
            if i == j:
                answer[i].append(1)
            else:
                answer[i].append(0)
    return answer