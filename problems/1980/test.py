from v1 import Solution

nums = ["01","10"]

s = Solution()
assert s.findDifferentBinaryString(nums) not in nums

nums = ["00","01"]

s = Solution()
assert s.findDifferentBinaryString(nums) not in nums

nums = ["111","011","001"]

s = Solution()
assert s.findDifferentBinaryString(nums) not in nums
