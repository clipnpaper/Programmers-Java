def solution(strArr: list[str]):
    answer = 0
    len_dic = {}
    for str in strArr:
        length = len(str)
        len_dic[length] = len_dic.get(length, 0) + 1
        answer = max(len_dic[length], answer)
    return answer