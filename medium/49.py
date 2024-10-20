# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for s in strs:
            sortedStr = "".join(sorted(s))

            if sortedStr in anagramDict:
                anagramDict[sortedStr].append(s)
            else:
                anagramDict[sortedStr] = [s]

        return list(anagramDict.values())
