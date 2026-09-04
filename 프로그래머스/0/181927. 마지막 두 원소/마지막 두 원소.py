def solution(num_list):
    answer = []
    length = len(num_list)
    idx = length - 2
    answer = num_list.copy()
    if num_list[idx] < num_list[idx+1]:
        answer.append(num_list[idx+1] - num_list[idx])
    else: 
        answer.append(2*num_list[idx+1])
    return answer