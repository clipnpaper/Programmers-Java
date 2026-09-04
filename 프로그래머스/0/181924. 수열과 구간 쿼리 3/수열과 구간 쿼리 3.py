def solution(arr, queries):
    answer = []

    for i, j in queries:
        num1 = arr[i]
        num2 = arr[j]
        arr[i] = num2
        arr[j] = num1
        
    answer = arr


    return answer