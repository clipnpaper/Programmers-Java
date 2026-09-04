def solution(numLog):
    answer = ''
    num0 = numLog[0]
    for idx in range(1, len(numLog)):
        control = numLog[idx] - numLog[idx-1]
        if control == 1:
            answer += 'w'
        elif control == -1:
            answer += 's'
        elif control == 10:
            answer += 'd'
        elif control == -10:
            answer += 'a'
            
    return answer