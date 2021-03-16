from typing import *
import functools

class Solution:
    def getIsEvenAndMedianIndex(self, length: int) -> (bool, int):
        even = length % 2 == 0
        return (even, length / 2 if even else (length + 1) / 2)

    def pickSmallest(self, nums: List[List[int]], pickable: List[bool], index: List[int]) -> int:
        pickable_remap = [i for i, v in enumerate(pickable) if v]

        ip = pickable_remap[0]
        sv = nums[ip][index[ip]]
        for i in pickable_remap:
            if nums[i][index[i]] < sv:
                ip = i
                sv = nums[i][index[i]]
        return ip

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [na for na in [nums1, nums2] if len(na) > 0]
        even, median_index = self.getIsEvenAndMedianIndex(functools.reduce(lambda l1, l2: l1 + l2, [len(a) for a in nums]))
        index, pickable, ip = ([0] * len(nums), [True] * len(nums), -1)

        while (median_index != 0):
            median_index -= 1

            if not ip < 0:
                pickable[ip] = index[ip] != (len(nums[ip]) - 1)
                if pickable[ip]:
                    index[ip] += 1
            ip = self.pickSmallest(nums, pickable, index)

        if not even:
            return nums[ip][index[ip]]
        else:
            m1 = nums[ip][index[ip]]
            pickable[ip] = index[ip] != (len(nums[ip]) - 1)
            if pickable[ip]:
                index[ip] += 1
            ip = self.pickSmallest(nums, pickable, index)
            return (m1 + nums[ip][index[ip]]) / 2


if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([], [2, 3], 2.5)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.findMedianSortedArrays(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.findMedianSortedArrays(t[0], t[1])
