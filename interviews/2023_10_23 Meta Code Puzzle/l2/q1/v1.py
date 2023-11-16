# Time Limit Exceeded on 5 test cases
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
    for a in a_:
        left_min, left_max = a - Y, a - X
        right_min, right_max = a + X, a + Y

        left_p, left_b = 0, 0
        right_p, right_b = 0, 0

        for p in p_:
            if p >= left_min and p <= left_max:
                left_p += 1
            elif p >= right_min and p <= right_max:
                right_p += 1

        for b in b_:
            if b >= left_min and b <= left_max:
                left_b += 1
            elif b >= right_min and b <= right_max:
                right_b += 1

        count += left_p * right_b + left_b * right_p

    return count
