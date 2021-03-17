from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2 = 0, 0
        result = []
        while i1 < m and i2 < n:
            if nums1[i1] < nums2[i2]:
                result.append(nums1[i1])
                i1 += 1
            else:
                result.append(nums2[i2])
                i2 += 1
        for i in range(i1, m):
            result.append(nums1[i])
        for i in range(i2, n):
            result.append(nums2[i])

        for i, num in enumerate(result):
            nums1[i] = num