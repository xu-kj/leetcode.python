from typing import List

# Write any import statements here


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    assert M == len(C)

    time = 0

    curr = 1
    for c in C:
        if c == curr:
            continue

        t1 = abs(curr - c)
        t2 = min(c, curr) + N - max(c, curr)
        time += min(t1, t2)

        curr = c

    return time
