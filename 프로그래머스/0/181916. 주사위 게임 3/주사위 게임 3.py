def solution(x1, x2, x3, x4):
    lis = [x1,x2,x3,x4]
    list = sorted(lis, reverse=True)
    a = list[0]
    b = list[1]
    c = list[2]
    d = list[3]

    if(a == b):
        if(c == d):
            if(a == c):
                return 1111*a
            else:
                return (a + c) * max(a-c, c-a)
        elif(b == c):
            return (10 * a + d) * (10 * a + d)
        else:
            return c * d
    elif(b==c):
        if(c == d):
            return (10 * b + a) * (10 * b + a)
        else:
            return a * d
    elif(c==d):
        return a * b
    else:
        return d