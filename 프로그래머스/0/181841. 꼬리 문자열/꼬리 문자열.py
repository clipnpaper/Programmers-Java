def is_suffix(str: str, ex:str):
    return True if str.find(ex) != -1 else False


def solution(str_list: list[str], ex: str):
    answer = ''
    for str in str_list:
        if is_suffix(str, ex):
            continue
        else:
            answer += str
    return answer