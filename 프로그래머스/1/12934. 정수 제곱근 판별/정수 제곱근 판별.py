import math

def solution(n: int):
    answer = math.sqrt(n)
    if answer == int(answer):
        answer += 1 
        return answer * answer
    else:
        return -1