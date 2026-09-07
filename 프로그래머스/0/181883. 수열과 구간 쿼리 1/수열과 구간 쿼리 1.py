def solution(arr: list[int], queries: list[int]):
    answer = arr
    for s, e in queries:
        for _ in range(s, e+1):
            answer[_] +=1 

    return answer