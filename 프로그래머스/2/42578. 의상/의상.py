def solution(clothes: list[list[str]]):
    answer = 1
    dic = {}
    for name, type in clothes:
        dic[type] = dic.get(type, 0) + 1

    for value in dic.values():
        answer *= value + 1

    return answer - 1

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))