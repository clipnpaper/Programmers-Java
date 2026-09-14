def solution(nums: list[str]):
    numbers = sorted(nums)

    for index in range(len(numbers) - 1):
        if numbers[index+1].startswith(numbers[index]): return False

    return True
