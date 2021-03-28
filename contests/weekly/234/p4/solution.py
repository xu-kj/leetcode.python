import math
import functools


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        def getNiceDivisors(num: int) -> int:
            c = primeFactors // num
            extra = primeFactors % num
            result = pow(c + 1, extra, int(1e9 + 7)) * \
                pow(c, num - extra, int(1e9 + 7))
            return result % int(1e9 + 7)

        def getNiceDivisorsDiffRatio(num1: int, num2: int) -> float:
            c1, e1 = primeFactors // num1, primeFactors % num1
            c2, e2 = primeFactors // num2, primeFactors % num2
            p1 = {
                c1 + 1: e1,
                c1: num1 - e1,
            }
            p1.copy()
            p2 = {
                c2 + 1: e2,
                c2: num2 - e2,
            }
            for k in p1:
                if k in p2:
                    p1[k], p2[k] = max(p1[k] - p2[k], 0), max(p2[k] - p1[k], 0)

            p1 = functools.reduce(lambda x, y: x * y,
                                  [k ** v for k, v in p1.items()])
            p2 = functools.reduce(lambda x, y: x * y,
                                  [k ** v for k, v in p2.items()])
            return p2 / p1

        left, right = 1, primeFactors // 2 + 1
        while left + 1 < right:
            mid = (left + right) // 2

            c_after = getNiceDivisorsDiffRatio(mid, mid + 1)
            c_before = getNiceDivisorsDiffRatio(mid - 1, mid)

            if c_before >= 1 and c_after <= 1:
                return getNiceDivisors(mid)
            elif c_before < 1:
                right = mid
            elif c_after > 1:
                left = mid + 1
        return getNiceDivisors(left) % int(1e9 + 7)


if __name__ == "__main__":
    test_cases = [
        (5, 6),
        (8, 18),
        (73, 572712676),
        (1, 1),
        (3, 3),
        (545918790, 421090465)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.maxNiceDivisors(t[0])
        if res != t[1]:
            sol.maxNiceDivisors(t[0])


# for small numbers:
# def maxNiceDivisors(self, primeFactors: int) -> int:
#     result = 1
#     for i in range(1, primeFactors // 2 + 1):
#         c = primeFactors // i
#         extra = primeFactors % i
#         result = max(result, (c + 1) ** extra * c ** (i - extra))
#     return int(result % (1e9 + 7))
#
# number of distinct prime factors -> result
# primeFactors 73
# 2: 1332
# 3: 14400
# 4: 110808
# 5: 661500
# 6: 3234816
# 7: 13310000
# 8: 47829690
# 9: 150994944
# 10: 421654016
# 11: 1067311728
# 12: 2539579392
# 13: 5248800000
# 14: 10546875000
# 15: 19531250000
# 16: 32000000000
# 17: 52428800000
# 18: 85899345920
# 19: 115964116992
# 20: 146767085568
# 21: 235092492288
# 22: 297538935552
# 23: 376572715308 <= max
# 24: 376572715308 <= max
# 25: 334731302496
# 26: 297538935552
# 27: 264479053824
# 28: 235092492288
# 29: 208971104256
# 30: 185752092672
# 31: 165112971264
# 32: 146767085568
# 33: 130459631616
# 34: 115964116992
# 35: 103079215104
