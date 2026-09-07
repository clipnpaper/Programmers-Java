def solution(my_string = str, m= int, c=int):
    answer = ''
    answer += my_string[c-1::m]
    return answer