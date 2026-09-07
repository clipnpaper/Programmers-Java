def solution(my_string, indices):
    arr = list(my_string)
    for idx in indices:
        arr[idx] = ""
    return "".join(arr)