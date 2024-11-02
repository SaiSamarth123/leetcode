# 345. Reverse Vowels of a String
# Easy
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiou")
        left, right = 0, len(s) - 1

        array = list(s)

        while left < right:
            if array[left].lower() not in vowels:
                left += 1
            elif array[right].lower() not in vowels:
                right -= 1
            else:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        return "".join(array)
