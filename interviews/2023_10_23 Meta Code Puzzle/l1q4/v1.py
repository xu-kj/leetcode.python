from typing import List

# Write any import statements here


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    assert M == len(C)

    time = 0

    curr = 1
    for c in C:
        if c > curr:
            forward = c - curr
            backward = N - c + curr
            time += min(forward, backward)
        elif c < curr:
            forward = N - curr + c
            backward = curr - c
            time += min(forward, backward)

        curr = c

    return time
