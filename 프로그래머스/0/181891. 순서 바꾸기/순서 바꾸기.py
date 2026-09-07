def solution(num_list: list[int], n: int):
    answer = num_list
    list1 = answer[n:]
    list2 = answer[:n]
    answer = list1 + list2
    return answer