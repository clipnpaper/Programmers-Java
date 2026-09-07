def solution(num_list: list[int]):
    answer = 0
    for _ in num_list:
        answer += nanugi(_)
    return answer

def nanugi(num: int):
    count = 0
    number = num
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number -=1
            number //= 2
        count += 1
    return count