def solution(num_str: str):
    answer = 0
    for ch in num_str:
        answer += int(ch)
    return answer