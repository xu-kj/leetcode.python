from typing import List

# Write any import statements here


# time limit exceeded for 1/33 test cases
def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    assert N == len(D)

    eaten = []
    eaten_ = set()
    eaten__ = 0

    for d in D:
        if d not in eaten_:
            eaten.append(d)
            if len(eaten) > K:
                removed = eaten.pop(0)
                eaten_.remove(removed)

            eaten_.add(d)
            eaten__ += 1

    return eaten__
