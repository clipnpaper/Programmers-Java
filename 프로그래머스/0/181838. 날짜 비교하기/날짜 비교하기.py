def solution(date1, date2):
    answer = 0
    date_1 = date1[0] * 365 + date1[1] * 12 + date1[2]
    date_2 = date2[0] * 365 + date2[1] * 12 + date2[2]
    answer = 1 if date1 < date2 else 0
    return answer