# Products of Array Discluding Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        sol = [1] * length

        pre = 1
        post = 1

        for i in range(length):

            sol[i] *= pre
            pre *= nums[i]

            sol[length - 1 - i] *= post
            post *= nums[length - 1 - i]

        return sol
