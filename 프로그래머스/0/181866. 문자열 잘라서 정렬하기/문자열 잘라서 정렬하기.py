def solution(myString):
    answer = []
    num_list = list(filter(None,myString.split('x')))
    answer = sorted(num_list)
    return answer