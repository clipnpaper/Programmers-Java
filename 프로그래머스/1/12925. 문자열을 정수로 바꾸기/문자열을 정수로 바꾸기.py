def solution(st: str):
    ch = st[0]
    if ch == '-':
        return -int(st[1:])
    return int(st)
    
if __name__ == "__main__":
    print(solution("-1234"))