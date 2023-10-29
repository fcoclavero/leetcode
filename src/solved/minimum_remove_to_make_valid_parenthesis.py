"""https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ('(' or ')', in any positions)
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

# Examples

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

# Constraints

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


class Solution:
    """
    Notes:
        - Remove minimum number of parenthesis to create valid string: multiple ways to
            create valid strings with same number of removals
    """

    def minRemoveToMakeValid(self, s: str) -> str:
        remove = []
        stack = []
        for i, c in enumerate(s):
            if c == ")":
                if len(stack) == 0:
                    remove.append(i)
                else:
                    stack.pop()
            elif c == "(":
                stack.append(i)

        res = ""
        last = 0
        for i in remove + stack:
            res += s[last:i]
            last = i + 1

        return res + s[last:]
