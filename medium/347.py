# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.


from typing import List


# O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        answer = sorted(count, key=count.get, reverse=True)

        return answer[:k]


# Solution with O(n) time complexity and space complexity using bucket sort
# count = {}
# bucket = [[] for i in range(len(nums) + 1)]
# result = []

# for num in nums:
#     count[num] = 1 + count.get(num, 0)

# for num, freq in count.items():
#     bucket[freq].append(num)

# for i in range(len(bucket) - 1, 0, -1):
#     if bucket[i]:
#         result.extend(bucket[i])

#     if len(result) == k:
#         return result
