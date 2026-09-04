def solution(arr, queries):
    answer = []

    for num in queries:
        s = num[0]
        e = num[1]
        k = num[2]
        min = 1_000_001
        for i in range(s, e+1):
           if i % k == 0:
               arr[i] += 1

    answer = arr
    return answer