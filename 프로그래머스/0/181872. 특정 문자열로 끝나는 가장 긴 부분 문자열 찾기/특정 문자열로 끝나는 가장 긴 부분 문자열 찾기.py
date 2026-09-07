def solution(myString: str, pat: str):
    answer = ''
    idx = myString.rfind(pat)
    answer = myString[:idx+len(pat)]
    return answer