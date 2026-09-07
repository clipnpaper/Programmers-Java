def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        for _ in range(0, slicer[1]+1):
            answer.append(num_list[_])
    elif n == 2: 
        for _ in range(slicer[0], len(num_list)):
            answer.append(num_list[_])
    elif n == 3:
        for _ in range(slicer[0], slicer[1]+1):
            answer.append(num_list[_])
    elif n == 4:
        for _ in range(slicer[0], slicer[1]+1, slicer[2]):
            answer.append(num_list[_])
    
    return answer