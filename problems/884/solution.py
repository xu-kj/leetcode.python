from typing import List
import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        sA = collections.Counter(A.split())
        sB = collections.Counter(B.split())
        for word in sA:
            if word in sB:
                sA[word] = 0
                sB[word] = 0
        uA = [word for word in sA.keys() if sA[word] == 1]
        uB = [word for word in sB.keys() if sB[word] == 1]
        return uA + uB

if __name__ == "__main__":
    test_cases = [
        ("this apple is sweet", "this apple is sour", ["sweet","sour"]),
        ("apple apple", "banana", ["banana"])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.uncommonFromSentences(t[0], t[1])
        tf = collections.Counter(res) == collections.Counter(t[2])
        if not tf:
            sol.uncommonFromSentences(t[0], t[1])
