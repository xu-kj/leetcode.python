from typing import List
from math import ceil


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    available = 0
    S_ = sorted(S)
    for i in range(M - 1):
        s1, s2 = S_[i], S_[i + 1]
        available_ = max(0, s2 - s1 - 1 - 2 * K)
        available += ceil(available_ / (K + 1))

    # first
    available_ = max(0, S_[0] - 1 - K)
    available += ceil(available_ / (K + 1))

    # last
    available_ = max(0, N - S_[-1] - K)
    available += ceil(available_ / (K + 1))

    return available
