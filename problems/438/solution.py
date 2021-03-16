from typing import List
import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        summary = collections.Counter(p)

        result = []
        for r in range(len(s)):
            if s[r] in summary:
                summary[s[r]] -= 1
            l = r - len(p)
            if l >= 0 and s[l] in summary:
                summary[s[l]] += 1
            if all([v <= 0 for v in summary.values()]):
                result.append(l + 1)
        return result