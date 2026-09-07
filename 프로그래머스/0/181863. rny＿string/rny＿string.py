def solution(rny_string: str):
    answer = ''
    for ch in rny_string:
        if ch == 'm':
            answer += "rn"
        else:
            answer += ch
            
    return answer