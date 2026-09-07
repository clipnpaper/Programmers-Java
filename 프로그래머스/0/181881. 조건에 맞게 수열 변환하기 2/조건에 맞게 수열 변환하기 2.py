def solution(arr: list[int]):
    arr1 = arr
    arr2 = []
    answer = 0
    while True:
        if answer % 2 == 0:
            arr2 = []
            for idx in range(len(arr)):
                num = arr1[idx]
                if num % 2 == 0 and num >= 50:
                    num //=2
                elif num % 2 == 1 and num < 50:
                    num = num * 2 + 1
                arr2.append(num)
        else:
            arr1 = []
            for idx in range(len(arr)):
                num = arr2[idx]
                if num % 2 == 0 and num >= 50:
                    num //=2
                elif num % 2 == 1 and num < 50:
                    num = num * 2 + 1
                arr1.append(num)
        if arr1 == arr2:
            return answer
        answer += 1
    return answer