def solution(arr, queries):
    answer = []

    for num in queries:
        s = num[0]
        e = num[1]
        k = num[2]
        min = 1_000_001
        for i in range(s, e+1):
            number = arr[i]
            if number > k and number < min:
                min = number
        if min == 1_000_001:
            answer.append(-1)
        else:
            answer.append(min)

    return answer