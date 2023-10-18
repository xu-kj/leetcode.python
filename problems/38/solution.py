from typing import *


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = ""
        prev = self.countAndSay(n - 1)
        rc, count = None, 0
        for c in prev:
            if c == rc:
                count += 1
            else:
                if rc:
                    result += f"{count}{rc}"
                rc, count = c, 1
        result += f"{count}{rc}"
        return result


if __name__ == "__main__":
    test_cases = [
        (1, "1"),
        (4, "1211"),
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.countAndSay(t[0])
        tf = res == t[1]
        if not tf:
            sol.countAndSay(t[0])
