def solution(nums: list[int]):
    answer = 0
    dic = {}
    N = len(nums) // 2
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    answer = min(len(dic), N)
    return answer



if __name__ == "__main__":
    print(solution())