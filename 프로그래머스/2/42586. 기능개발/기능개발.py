from collections import deque

def solution(progresses: list[int], speeds: list[int]):
    answer = []
    days = deque()
    for progress, speed in zip(progresses, speeds):
        day = (100-progress) // speed
        if (100-progress) % speed != 0:
            day += 1
        days.append(day)

    maxDay = 0
    count = 0
    while days:
        day = days.popleft()
        if(day > maxDay):
            maxDay = day
            if(count != 0):
                answer.append(count)
            count = 1
        else: 
            count += 1
    if(count != 0):
        answer.append(count)

    return answer

if __name__ == "__main__":
    print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))