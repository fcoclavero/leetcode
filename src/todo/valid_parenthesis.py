"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

# Examples

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

# Constraints

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    """
    - Use stack to push opening parenthesis
    - Pop when we encounter closing parenthesis. If not matching, return false.
    - O[n]

    # Examples

    s = "([]{()"
    """
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for c in s:
            if c in parenthesis.values():  # opening parenthesis
                stack.append(c)
            elif len(stack) == 0 or parenthesis[c] != stack.pop():
                return False

        return len(stack) == 0
