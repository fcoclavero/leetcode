"""
Given a string s, return true if the s can be palindrome after deleting at most one
character from it.

# Examples

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    """
    Notes:
        - O[len(s)]
    """

    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(string: str) -> bool:  # "ab"
            i = 0
            j = len(string) - 1

            while i < j:
                if string[i] != string[j]:
                    return False

                i += 1
                j -= 1

            return True

        # "ab"
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return is_palindrome(s[i + 1: j]) or is_palindrome(s[i: j - 1])

            i += 1
            j -= 1

        return True
