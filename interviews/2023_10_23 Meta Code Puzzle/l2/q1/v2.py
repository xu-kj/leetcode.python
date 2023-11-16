# Time Limit Exceeded on 5 test cases
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    assert N == len(C)

    lp, lb = 0, 0
    rp, rb = 0, 0

    for c in C[X - 1:Y]:
        if c == "P":
            rp += 1
        elif c == "B":
            rb += 1

    count = 0
    for i, c in enumerate(C):
        rr, rl = i + Y, i + X - 1
        lr, ll = i - X, i - Y - 1

        p, b = process(rr, C)
        rp += p
        rb += b

        p, b = process(rl, C)
        rp -= p
        rb -= b

        p, b = process(lr, C)
        lp += p
        lb += b

        p, b = process(ll, C)
        lp -= p
        lb -= b

        if c == "A":
            count += lp * rb + lb * rp

    return count


def process(i: int, C: str):
    if i >= 0 and i < len(C):
        if C[i] == "P":
            return 1, 0
        elif C[i] == "B":
            return 0, 1

    return 0, 0
