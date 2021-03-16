from typing import *


class Solution:
    def canFormString(self, source: str, target: str) -> bool:
        if len(source) < len(target):
            return False
        for c in target:
            if c in source:
                source = source[source.index(c)+1:]
            else:
                return False
        return True

    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = []
        for ss in d:
            if self.canFormString(s, ss):
                res.append(ss)
        if res:
            if len(res) > 1:
                res.sort(key=len, reverse=True)
                res = [s for s in res if len(s) == len(res[0])]
                res.sort()
            return res[0]
        else:
            return ""


if __name__ == "__main__":
    test_cases = [
        ("abpcplea", ["ale", "apple", "monkey", "plea"], "apple"),
        ("abpcplea", ["a", "b", "c"], "a"),
        ("apple", ["zxc", "vbn"], "")
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.findLongestWord(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.findLongestWord(t[0], t[1])
