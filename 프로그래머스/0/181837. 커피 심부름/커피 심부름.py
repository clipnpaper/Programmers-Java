def solution(order: list[str]):
    answer = 0
    for ord in order:
        if ord == "icecafelatte" or ord == "cafelatteice" or ord == "hotcafelatte" or ord == "cafelattehot" or ord == "cafelatte":
            answer += 5000
        else:
            answer += 4500
    return answer