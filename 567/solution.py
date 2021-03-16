import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        summary = collections.Counter(s1)
        for i in range(len(s2)):
            if s2[i] in summary:
                summary[s2[i]] -= 1
            l = i - len(s1)
            if l >= 0 and s2[l] in summary:
                summary[s2[l]] += 1

            if all([v <= 0 for v in summary.values()]):
                return True
        return False

if __name__ == "__main__":
    test_cases = [
        ('ab', 'eidboaoo', False),
        ('ab', 'eidbaooo', True),
        ('hello', 'ooolleoooleh', False),
        ('adc', 'dcda', True),
        ('abc', 'ccccbbbbaaaa', False)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.checkInclusion(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.checkInclusion(t[0], t[1])
