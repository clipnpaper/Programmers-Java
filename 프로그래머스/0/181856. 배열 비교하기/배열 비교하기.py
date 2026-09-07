def solution(arr1: list[int], arr2: list[int]):
    answer = 0
    if (len(arr1) > len(arr2)):
        answer = 1
    elif(len(arr1) < len(arr2)):
        answer = -1
    else:
        total1=0
        total2=0
        for idx in range(len(arr1)):
            total1 += arr1[idx]
            total2 += arr2[idx]
        if total1 > total2:
            answer = 1
        elif total1 < total2:
            answer = -1
        else:
            answer = 0
    return answer