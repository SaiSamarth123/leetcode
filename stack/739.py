# Daily Temperatures
# Medium
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answer = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prevIndex = stack.pop()
                answer[prevIndex] = index - prevIndex
            stack.append(index)
        return answer
