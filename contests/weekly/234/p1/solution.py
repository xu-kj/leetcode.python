import string


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        number = ""
        numbers = set()
        for c in word:
            if c not in string.digits:
                if number:
                    numbers.add(int(number))
                    number = ""
            else:
                number += c

        if number:
            numbers.add(int(number))

        return len(numbers)


"a123bc34d8ef34", 3
"leet1234code234", 2
"a1b01c001", 1

if __name__ == "__main__":
    test_cases = [
        (4, 2, 6, 2),
        (6, 1, 10, 3),
        (6, 1, 14, 4),
        (1, 0, 24, 24),
        (9, 0, 90924720, 10102750), # O(n * maxSum) -> O(n * log(maxSum))
        (8257285, 4828516, 850015631, 29014) # O(n * log(maxSum)) -> O(log(maxSum))
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.maxValue(t[0], t[1], t[2])
        if res != t[3]:
            sol.maxValue(t[0], t[1], t[2])

