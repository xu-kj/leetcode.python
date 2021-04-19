import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = {}
        for c in string.ascii_lowercase:
            counter[c] = 0

        for c in sentence:
            counter[c] += 1

        return all([v > 0 for v in counter.values()])


if __name__ == "__main__":
    test_cases = [
        ("thequickbrownfoxjumpsoverthelazydog"),
        ("leetcode")
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.checkIfPangram(t[0])
        if res != t[1]:
            sol.checkIfPangram(t[0])
