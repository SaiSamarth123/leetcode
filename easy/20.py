# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parenthesis = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in parenthesis:
                if stack and stack[-1] == parenthesis[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
