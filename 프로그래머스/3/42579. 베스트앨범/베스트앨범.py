
def solution(genres: list[str], plays: list[int]):
    # {장르 : {고유번호 :재생 횟수}}
    #{"classic" : {0: 500, 2: 150, 3: 800}, "pop" : {1: 600, 4:2500}}
    answer = []
    dic = {}
    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic:
            dic[genre] = {}
        dic[genre][index] = play

    def get_genre_total(genre: str) -> int:
        return sum(dic[genre].values())
    # 사용
    sorted_genres = sorted(dic.keys(), key=get_genre_total, reverse=True)

    # 2. 각 장르 내에서 노래 정렬 후 최대 2개 추출
    for genre in sorted_genres:
        songs = dic[genre]  # {고유번호: 재생수}
        # 재생수 내림차순(-x[1]), 번호 오름차순(x[0])
        sorted_songs = sorted(songs.items(), key=lambda x: (-x[1], x[0]))
        
        # 상위 최대 2곡의 고유번호만 answer에 추가
        for idx, _ in sorted_songs[:2]:
            answer.append(idx)

    return answer

if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))