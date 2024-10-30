# Is Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.


import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        input = "".join(ch.lower() for ch in s if ch.isalnum())

        i = 0
        j = len(input) - 1

        while i < j:
            if input[i] != input[j]:
                return False
            i += 1
            j -= 1

        return True
