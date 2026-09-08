def solution(a: int, b: int):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:
        return a * a + b * b
    elif a % 2 != 0 or b % 2 != 0:
        return 2 * (a + b)
    else:
        return max(a - b, b-a )
    return answer