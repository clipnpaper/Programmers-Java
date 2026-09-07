def solution(my_strings, parts):
    answer = ''
    i = 0
    for start, end in parts:
        str = my_strings[i][start:end+1]
        answer += str
        i += 1
    return answer