def solution(num_list):
    answer = 0
    total1 = 0
    total2 = 0
    for idx in range(len(num_list)):
        if idx % 2 == 0:
            total1 += num_list[idx]
        else:
            total2 += num_list[idx]
    answer = max(total1, total2)
    return answer