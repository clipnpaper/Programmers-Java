def solution(str_list: list[str]):
    answer = []
    for idx in range(len(str_list)):
        ch = str_list[idx]
        if ch == "l":
            answer = str_list[:idx]
            return answer
        elif ch == "r":
            answer = str_list[idx+1:]
            return answer
    return answer
