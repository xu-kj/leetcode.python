from v1 import Solution

test_cases = [
    (
        [1, 2, 2, 1], [2, 2],
        [2]
    ),
    (
        [4, 9, 5], [9, 4, 9, 8, 4],
        [9, 4]
    ),
]

def equivalentArray(nums1, nums2):
    for e in nums1:
        if e not in nums2:
            return False
    for e in nums2:
        if e not in nums1:
            return False

    return True

for nums1, nums2, expected in test_cases:
    res = Solution().intersection(nums1, nums2)

    f = True
    for e in expected:
        if e not in res:
            f = False
            break
    for e in res:
        if e not in expected:
            f = False
            break
    if not equivalentArray(res, expected):
        Solution().intersection(nums1, nums2)
