def solution(myString: str, pat: str):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:].startswith(pat):
            answer += 1
    return answer