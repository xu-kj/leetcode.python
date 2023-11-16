from v2 import getMaximumEatenDishCount

N = 6
D = [1, 2, 3, 3, 2, 1]
K = 1

assert 5 == getMaximumEatenDishCount(N, D, K)

N = 6
D = [1, 2, 3, 3, 2, 1]
K = 2

assert 4 == getMaximumEatenDishCount(N, D, K)

N = 7
D = [1, 2, 1, 2, 1, 2, 1]
K = 2

assert 2 == getMaximumEatenDishCount(N, D, K)
