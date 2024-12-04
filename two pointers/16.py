# 16. 3Sum Closest
# Medium

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.


from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closestSum = float("inf")

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == target:
                    return currentSum

                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum

                if currentSum < target:
                    left += 1
                else:
                    right -= 1

        return closestSum
