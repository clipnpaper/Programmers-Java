def solution(s: str):
    words = s.split(" ")
    return " ".join(word.capitalize() for word in words)