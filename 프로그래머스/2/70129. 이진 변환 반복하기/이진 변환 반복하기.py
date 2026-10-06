def solution(s):
    answer = []
    zero_count = 0
    count = 0
    while s != "1":
        zero_count += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        count += 1
    
    answer.append(count)
    answer.append(zero_count)
    return answer