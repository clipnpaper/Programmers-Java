def solution(myString: str, pat: str):
    answer = 0
    long_str = myString.lower()
    short_str = pat.lower()
    flag = long_str.find(short_str)
    answer = 1 if flag != -1 else 0
    return answer