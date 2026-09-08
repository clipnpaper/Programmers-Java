def solution(num_list: list[int], n: int):
    answer = 0
    try:
        num_list.index(n)
    except ValueError:
        return 0
    return 1