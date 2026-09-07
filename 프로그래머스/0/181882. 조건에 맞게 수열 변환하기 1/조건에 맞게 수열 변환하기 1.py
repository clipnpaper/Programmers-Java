def solution(arr: list[int]):
    answer = []
    for num in arr:
        if num % 2 == 0 and num >= 50:
            num //=2
        elif num % 2 == 1 and num < 50:
            num *= 2
        answer.append(num)
    return answer