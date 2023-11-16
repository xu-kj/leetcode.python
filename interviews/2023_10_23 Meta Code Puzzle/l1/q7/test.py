from v1 import getUniformIntegerCountInInterval

A = 75
B = 300

assert getUniformIntegerCountInInterval(A, B) == 5

A = 1
B = 9

assert getUniformIntegerCountInInterval(A, B) == 9

A = 999999999999
B = 999999999999

assert getUniformIntegerCountInInterval(A, B) == 1
