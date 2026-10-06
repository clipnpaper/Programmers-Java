def solution(arr):
    answer = arr[0]
    for num in arr[1:]:
        answer = answer * num // gcd(max(answer, num),min(answer, num))
    
    return answer

def gcd(high_num: int, low_num: int):
    if(high_num % low_num == 0): return low_num
    return gcd(low_num, high_num % low_num)