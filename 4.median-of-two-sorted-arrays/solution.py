from typing import *


class Solution:
    def getIsEvenAndMedianIndex(self, length: int) -> (bool, int):
        even = length % 2 == 0
        return (even, int((length / 2 if even else (length + 1) / 2) - 1))

    def getMedian(self, nums: List[int], even: bool, index: int) -> float:
        return (nums[index] + nums[index + 1]) / 2 if even else nums[index]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        even, median_index = self.getIsEvenAndMedianIndex(len(nums1) + len(nums2))
        pickable = [len(nums1) > 0, len(nums2) > 0]

        if not pickable[0]:
            return self.getMedian(nums2, even, median_index)
        if not pickable[1]:
            return self.getMedian(nums1, even, median_index)

        nums = [nums1, nums2]
        index, ip = ([0, 0], 0 if nums1[0] < nums2[0] else 1)
        while (median_index != 0):
            median_index -= 1

            if index[ip] == (len(nums[ip]) - 1):
                pickable[ip] = False
                ip = 1 - ip
                continue
            else:
                index[ip] += 1
                if pickable[1 - ip] and nums[1 - ip][index[1 - ip]] < nums[ip][index[ip]]:
                    ip = 1 - ip

        if not even:
            return nums[ip][index[ip]]
        else:
            m1 = nums[ip][index[ip]]
            if index[ip] != (len(nums[ip]) - 1):
                m2 = min(nums[ip][index[ip] + 1], nums[1 - ip][index[1 - ip]]) if pickable[1 - ip] else nums[ip][index[ip] + 1]
                return (m1 + m2) / 2
            else:
                m2 = nums[1 - ip][index[1 - ip]]
                return (m1 + m2) / 2


if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([], [2, 3], 2.5),
        ([1, 2], [-1, 3], 1.5),
        ([1], [2, 3, 4], 2.5)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.findMedianSortedArrays(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.findMedianSortedArrays(t[0], t[1])
