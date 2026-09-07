def solution(myString: str,  pat : str):
    myStr = ""
    for ch in myString:
        if ch == 'A':
            myStr += "B"
        else:
            myStr += "A"
    answer = 1 if myStr.find(pat) != -1 else 0
    return answer