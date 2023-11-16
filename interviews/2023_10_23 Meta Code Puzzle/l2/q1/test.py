from v2 import getArtisticPhotographCount

N = 5
C = "APABA"
X = 1
Y = 2

assert getArtisticPhotographCount(N, C, X, Y) == 1

N = 5
C = "APABA"
X = 2
Y = 3

assert getArtisticPhotographCount(N, C, X, Y) == 0

N = 8
C = ".PBAAP.B"
X = 1
Y = 3

assert getArtisticPhotographCount(N, C, X, Y) == 3
