from v1 import getMinProblemCount

N = 6
S = [1, 2, 3, 4, 5, 6]

assert getMinProblemCount(N, S) == 4

N = 4
S = [4, 3, 3, 4]

assert getMinProblemCount(N, S) == 3

N = 4
S = [2, 4, 6, 8]

assert getMinProblemCount(N, S) == 4
