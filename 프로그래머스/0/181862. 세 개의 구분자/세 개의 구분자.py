def solution(myStr: str):
    answer = []
    addStr = ""
    for ch in myStr:
        if ch == "a" or ch == "b" or ch == "c":
            answer.append(addStr)
            addStr = ""
        else: 
            addStr += ch
    answer.append(addStr)
    answer=list(filter(None, answer))
    if not answer:
        answer.append("EMPTY")
    return answer