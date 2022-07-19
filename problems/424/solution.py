from typing import *


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_by_character = {}
        max_total_characters = 0
        l = 0
        for c in s:
            if c in count_by_character:
                count_by_character[c] += 1
            else:
                count_by_character[c] = 1

            while sum(count_by_character.values()) - max(count_by_character.values()) > k:
                count_by_character[s[l]] -= 1
                l += 1

            max_total_characters = max(max_total_characters, sum(count_by_character.values()))
        return max_total_characters


if __name__ == "__main__":
    test_cases = [
        (
            "ABAB", 2,
            4
        ),
        (
            "AABABBA", 1,
            4
        ),
    ]

    sol = Solution()
    for s, k, expected in test_cases:
        res = sol.characterReplacement(s, k)
        if res != expected:
            sol.characterReplacement(s, k)
