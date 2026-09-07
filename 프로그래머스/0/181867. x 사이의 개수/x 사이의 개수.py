def solution(myString: str):
    answer = []
    count = 0
    for ch in myString:
        if ch == 'x':
            answer.append(count)
            count = 0
        else:
            count += 1
    answer.append(count)
    
    return answer