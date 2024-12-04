# 2461. Maximum Sum of Distinct Subarrays With Length K
# Medium
# You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        windowSum, windowStart, maxSum = 0, 0, 0

        unique = {}

        for windowEnd in range(len(nums)):

            num = nums[windowEnd]
            windowSum += num
            unique[num] = unique.get(num, 0) + 1

            if windowEnd - windowStart + 1 == k:

                if len(unique) == k:
                    maxSum = max(windowSum, maxSum)

                windowSum -= nums[windowStart]
                unique[nums[windowStart]] -= 1

                if unique[nums[windowStart]] == 0:
                    del unique[nums[windowStart]]

                windowStart += 1

        return maxSum
