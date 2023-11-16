from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_ = [int(num, 2) for num in nums]

        num = 0
        while True:
            if num not in nums_:
                binary_form = bin(num)[2:]
                binary_form = (len(nums) - len(binary_form)) * "0" + binary_form
                return binary_form
            num += 1
