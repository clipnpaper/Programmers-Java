def solution(picture: list[str], k: int):
    answer = []
    for str in picture:
        str1 = ""
        for ch in str:
            for _ in range(k):
                str1 += ch 
        for _ in range(k):
            answer.append(str1)
    return answer