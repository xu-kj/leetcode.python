from typing import List

# Write any import statements here


def getMinProblemCount(N: int, S: List[int]) -> int:
    assert N == len(S)

    s_max = max(S)
    count = s_max // 2

    modulos = [s % 2 for s in S]
    count += 1 if sum(modulos) > 0 else 0

    return count
