# 1832. Check if the Sentence Is Pangram
# Easy
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        return len(set(sentence)) == 26

        # seen = set()

        # for char in sentence:

        #     if char.isalpha():
        #         seen.add(char.lower())

        # if len(seen) == 26:
        #     return True

        # return False
