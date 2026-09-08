def naseon(answer: list[list[int]], n: int):
    lis = answer
    arrow = [[0, 1], [1,0], [0,-1], [-1,0],]
    arrow_index = 0
    x = 0
    y = 0
    for index in range(1, n*n+1):
        lis[x][y] = index

        check_x = arrow[arrow_index][0] + x
        check_y = arrow[arrow_index][1] + y

        if check_x < 0 or check_x >= n or check_y < 0 or check_y >= n:
            # 방향 변경
            arrow_index = arrow_index + 1
            arrow_index = arrow_index % 4
        elif lis[check_x][check_y] != 0 :
            arrow_index = arrow_index + 1
            arrow_index = arrow_index % 4
        x += arrow[arrow_index][0]
        y += arrow[arrow_index][1]
    return lis



def solution(n: int):
    answer = [[]]
    for i in range(n):
        if i != n-1: answer.append([])
        for j in range(n):
            answer[i].append(0)
    lis = naseon(answer, n)

    return lis