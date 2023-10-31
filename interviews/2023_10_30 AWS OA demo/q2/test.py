from v1 import countGroups

testcases = [
    (["110", "110", "001"], 2),
    (["1100", "1110", "0110", "0001"], 2),
    (["10000", "01000", "00100", "00010", "00001"], 5),
    (["10100", "01010", "10100", "01010", "00001"], 3),
]

for testcase in testcases:
    matrix, expected = testcase
    result = countGroups(matrix)
    print(f"{result=}")
