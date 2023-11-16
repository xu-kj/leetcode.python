def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    assert N == len(C), f"{N=}, {len(C)=}"

    p_, a_, b_ = [], [], []
    for i, c in enumerate(C):
        if c is "P":
            p_.append(i)
        elif c is "A":
            a_.append(i)
        elif c is "B":
            b_.append(i)

    count = 0

    # P-A-B
    for p in p_:
        a_min, a_max = p + X, p + Y
        b_min_, b_max_ = a_min + X, a_max + Y
        a__ = [a for a in a_ if a >= a_min and a <= a_max]
        b__ = [b for b in b_ if b >= b_min_ and b <= b_max_]
        for a in a__:
            b_min, b_max = a + X, a + Y
            b___ = [b for b in b__ if b >= b_min and b <= b_max]
            count += len(b___)

    # B-A-P
    for b in b_:
        a_min, a_max = b + X, b + Y
        p_min_, p_max_ = a_min + X, a_max + Y
        a__ = [a for a in a_ if a >= a_min and a <= a_max]
        p__ = [p for p in p_ if p >= p_min_ and p <= p_max_]
        for a in a__:
            p_min, p_max = a + X, a + Y
            p___ = [p for p in p__ if p >= p_min and p <= p_max]
            count += len(p___)

    return count
