def solution(participant: list[str], completion: list[str]):
    answer = ''
    party = {}
    for name in participant:
        party[name] = party.get(name, 0) + 1

    for name in completion:
        if party[name] == 1:
            del party[name]
        elif party[name] >= 2:
            party[name] -= 1

    for key in party:
        answer += key
    return answer
    



if __name__ == "__main__":
    print(solution())