def solution(my_string = str, s= int, e=int):
    answer = ''
    answer += my_string[:s]
    answer += my_string[s:e+1][::-1]
    answer += my_string[e+1:]
    return answer