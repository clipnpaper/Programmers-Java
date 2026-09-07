def solution(binomial: str):
    answer = 0
    a, op, b = binomial.split()
    num1 = int(a)
    num2 = int(b)
    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2

    return answer