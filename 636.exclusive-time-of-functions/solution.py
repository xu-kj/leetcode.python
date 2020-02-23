from typing import *


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ft = {}
        t = []
        for log in logs:
            log = log.split(":")
            id = int(log[0])
            time = int(log[-1])
            state = log[1]

            if state == "start":
                # assume id will always match, no need to save and check
                t.append([time, 0])
            elif state == "end":
                start = t.pop()
                d = time + 1 - start[0]
                di = start[1]
                if id in ft:
                    ft[id] += d - di
                else:
                    ft[id] = d - di
                if len(t) > 0:
                    t[-1][1] += d
        ids = list(ft.keys())
        ids.sort()
        result = [ft[id] for id in ids]
        return result


if __name__ == "__main__":
    test_cases = [
        (
            [
                "0:start:0",
                "1:start:2",
                "1:end:5",
                "0:end:6",
            ], [3,4]
        ),
        (
            [
                "0:start:0",
                "0:start:2",
                "0:end:5",
                "0:start:6",
                "0:end:6",
                "0:end:7",
            ], [8]
        ),
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.exclusiveTime(len(t[0]), t[0])
        if res != t[1]:
            sol.exclusiveTime(len(t[0]), t[0])
