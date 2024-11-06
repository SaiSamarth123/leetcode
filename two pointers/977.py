# 977. Squares of a Sorted Array
# Easy
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)

        squares = [0 for x in range(n)]

        highestSquare = n - 1

        left, right = 0, n - 1

        while left <= right:

            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]

            if leftSquare > rightSquare:
                squares[highestSquare] = leftSquare
                left += 1
            else:
                squares[highestSquare] = rightSquare
                right -= 1

            highestSquare -= 1

        return squares
