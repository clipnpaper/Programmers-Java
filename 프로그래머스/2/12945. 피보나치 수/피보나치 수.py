def solution(n):
    answer = 0
    dp = [0]
    dp.append(1)
    for _ in range(2,100_001):
        dp.append((dp[-1] + dp[-2]) % 1234567)
    return dp[n]