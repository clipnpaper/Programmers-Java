def solution(my_string):
    answer = []
    for ch in range(0,len(my_string)):
        answer.append(my_string[-ch:])
    answer2 = sorted(answer)
    return answer2