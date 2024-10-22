# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):

            j = i
            # can also use the method find to simplify code
            # j = find('#', i)
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1

            res.append(s[i : i + length])

            i += length

        return res
