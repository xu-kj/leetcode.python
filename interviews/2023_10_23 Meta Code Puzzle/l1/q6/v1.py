from typing import List

# Write any import statements here


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    assert N == len(R)

    deflate = 0
    for i in reversed(range(len(R))):
        r = R[i]
        if r - i <= 0:
            return -1

        if i + 1 < len(R) and r >= R[i + 1]:
            deflate += 1
            R[i] = R[i + 1] - 1

    return deflate
