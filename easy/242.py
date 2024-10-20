# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t):
            return True

        return False
