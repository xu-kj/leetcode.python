import math


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # time complexity: O(n)
        # def getMinSum(indexElement):
        #     array = [indexElement] * n
        #     for i, element in enumerate(array):
        #         array[i] = max(1, element - abs(i - index))
        #     return sum(array)

        # time complexity: O(1)
        def getMinSum(indexElement):
            array_sum = 0
            for i in [0, n - 1]:
                element = max(1, indexElement - abs(i - index))
                array_sum += (element + indexElement) * (indexElement - element + 1) / 2
                array_sum += abs(index - i) + 1 - (indexElement - element + 1)
            array_sum -= indexElement
            return array_sum

        l, r = 1, maxSum + 1
        while l < r - 1:
            mid = int((l + r) / 2)
            min_sum = getMinSum(mid)
            if min_sum > maxSum:
                r = mid
            elif min_sum < maxSum:
                l = mid
            else:
                return mid
        return l


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
