def solution(num_list: list[int]):
    answer = -1
    for _ in num_list:
        if _ < 0:
            return num_list.index(_)
    return answer