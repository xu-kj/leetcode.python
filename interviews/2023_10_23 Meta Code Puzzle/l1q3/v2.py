from typing import List

# Write any import statements here


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    assert N == len(D)

    eaten = []
    eaten_ = set()

    for d in D:
        if d not in eaten_:
            eaten.append(d)
            eaten_.add(d)
            if len(eaten) > K:
                eaten_.remove(eaten[-K - 1])

    return len(eaten)
