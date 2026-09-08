def solution(arr: list[int], delete_list: list[int]):
    answer = arr
    for num in delete_list:
        try:
            answer.remove(num)
        except ValueError:
            continue
    return answer