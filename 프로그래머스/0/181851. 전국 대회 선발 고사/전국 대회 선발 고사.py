def sort_key(x):
    if x["참석"]:
        return x["등수"]
    else:
        return 10001

def solution(rank: list[int], attendance: list[bool]):
    answer = 0
    rank_list = []
    for idx in range(len(rank)):
        dic = {"인덱스": idx, "등수": rank[idx], "참석": attendance[idx]}
        rank_list.append(dic)
    sorted_list = sorted(rank_list, key=sort_key)
    a = sorted_list[0]["인덱스"]
    b = sorted_list[1]["인덱스"]
    c = sorted_list[2]["인덱스"]
    answer = 10000*a + 100*b + c
    return answer