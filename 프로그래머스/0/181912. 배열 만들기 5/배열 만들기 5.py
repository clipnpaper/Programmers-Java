def solution(intStrs, k, s, l):
    answer = []
    for intStr in intStrs:
        str = intStr[s:s+l]
        if int(str) > k:
            answer.append(int(str))
    return answer