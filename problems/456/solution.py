from collections import deque
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        results = deque()
        for i, num in enumerate(nums):
            if not results:
                results.append((num, num))  # (low, high)
                continue

            add_back = deque()
            while results:
                lower, upper = results.pop()

                if num <= lower:
                    if num < lower and not add_back: # num is a new lowerbound, cannot use existing upperbound(s), start a new scope
                        add_back.append((num, num))

                    add_back.append((lower, upper))
                    break # everything else in results has a upperbound > num, no need to process

                elif num >= upper:
                    if not add_back: # add_back already contains a pair with a lower lowerbound, and a higher (or equal) upperbound
                        add_back.append((lower, num))
                    continue

                else:
                    return True

            while add_back:
                results.append(add_back.pop())

        return False


if __name__ == "__main__":
    test_cases = [
        (
            [1, 2, 3, 4],
            False
        ),
        (
            [3, 1, 4, 2],
            True
        ),
        (
            [-1, 3, 2, 0],
            True
        ),
        (
            [1, 0, 1, -4, -3],
            False
        ),
        (
            [3, 5, 0, 3, 4],
            True
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.find132pattern(t[0])
        tf = res == t[1]
        if not tf:
            sol.find132pattern(t[0])
