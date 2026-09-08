def solution(my_string: str, target: str):
    answer = 0
    answer = 1 if my_string.find(target) != -1 else 0
    return answer