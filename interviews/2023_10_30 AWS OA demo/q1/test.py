from v1 import processLogs

testcases = [
    (["88 99 200", "88 99 300", "99 32 100", "12 12 15"], 2, ["88, 99"]),
]

for testcase in testcases:
    logs, threshold, expected = testcase
    result = processLogs(logs, threshold)
    print(f"{result=}")
