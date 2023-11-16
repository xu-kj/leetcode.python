from v1 import getMinCodeEntryTime

N = 3
M = 3
C = [1, 2, 3]

assert getMinCodeEntryTime(N, M, C) == 2

N = 10
M = 4
C = [9, 4, 4, 8]

assert getMinCodeEntryTime(N, M, C) == 11
