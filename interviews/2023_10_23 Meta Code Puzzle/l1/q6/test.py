from v1 import getMinimumDeflatedDiscCount

N = 5
R = [2, 5, 3, 6, 5]

assert getMinimumDeflatedDiscCount(N, R) == 3

N = 3
R = [100, 100, 100]

assert getMinimumDeflatedDiscCount(N, R) == 2

N = 4
R = [6, 5, 4, 3]

assert getMinimumDeflatedDiscCount(N, R) == -1
