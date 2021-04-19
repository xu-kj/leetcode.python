from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        counter = 0
        for cost in sorted_costs:
            if cost > coins:
                break

            counter += 1
            coins -= cost

        return counter


if __name__ == "__main__":
    test_cases = [
        (
            [1, 3, 2, 4, 1],
            7,
            4
        ),
        (
            [10, 6, 8, 7, 7, 8],
            5,
            0
        ),
        (
            [1, 6, 3, 1, 2, 5],
            20,
            6
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.checkIfPangram(t[0])
        if res != t[1]:
            sol.checkIfPangram(t[0])
