from typing import List


# XOR law with AND:
# x & (y ^ z) = (x & y) ^ (x & z)
#
# for [a1, a2, ..., ai] and [b1, b2, ..., bj]
# result
#   = (a1 & b1) ^ (a1 & b2) ^ ... ^ (a1 & bj) ^ ... ^ (ai & b1) ^ ... ^ (ai & bj)
#   = (a1 & (b1 ^ b2 ^ ... ^ bj)) ^ ... ^ (ai & (b1 ^ b2 ^ ... ^ bj))
#   = (b1 ^ b2 ^ ... ^ bj) & (a1 ^ a2 ^ ... ^ ai)
# getting these 2 XOR results is O(n), n <= 10^5
# smaller than 10^6

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor_1, xor_2 = 0, 0
        for item in arr1:
            xor_1 ^= item
        for item in arr2:
            xor_2 ^= item
        return xor_1 & xor_2


if __name__ == "__main__":
    test_cases = [
        (
            [1, 2, 3],
            [6, 5],
            0
        ),
        (
            [12],
            [4],
            4
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.getXORSum(t[0], t[1])
        if res != t[2]:
            sol.getXORSum(t[0], t[1])
