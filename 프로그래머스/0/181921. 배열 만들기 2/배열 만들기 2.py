from itertools import product

def solution(l, r):
    result = [] 
    for length in range(1, 7):
        for digits in product(['0', '5'], repeat=length):
            num = int("".join(digits))
            if num <= r and num >= l and num not in result:
                result.append(num)

    result1 = sorted(result)
    if len(result1) == 0: return [-1]
    return result1