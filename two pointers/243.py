# Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
# Easy


class Solution:
    def shortestDistance(self, words, word1, word2):
        # TODO: Write your code here

        shortestDistance = len(words)
        pos1, pos2 = -1, -1

        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
            elif word == word2:
                pos2 = i

            if pos1 != -1 and pos2 != -1:
                shortestDistance = min(shortestDistance, abs(pos1 - pos2))

        return shortestDistance
