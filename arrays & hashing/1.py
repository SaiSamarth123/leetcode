# 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in numMap:
                return [numMap[complement], i]

            numMap[num] = i

        return []
