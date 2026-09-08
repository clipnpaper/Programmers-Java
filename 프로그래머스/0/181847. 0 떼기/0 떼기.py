def solution(n_str: str):
    answer = ''
    idx = 0
    for ch in n_str:
        if ch != '0':
            break
        idx += 1
    for i in range(idx, len(n_str)):
        answer += n_str[i]
    return answer