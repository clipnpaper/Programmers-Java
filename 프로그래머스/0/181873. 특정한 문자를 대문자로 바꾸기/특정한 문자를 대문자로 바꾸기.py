def solution(myString: str, alp: str):
    answer = ''
    for ch in myString:
        if ch == alp:
            answer += ch.upper()
        else:
            answer += ch
    return answer