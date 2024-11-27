"""https://leetcode.com/problems/merge-strings-alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d

# Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

class Solution:  # 39 ms
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longest = word1 if len(word1) >= len(word2) else word2
        shortest = word2 if longest == word1 else word1

        buffer = []

        for i, j in zip(word1, word2):
            buffer.append(i + j)

        buffer.append(longest[len(shortest):])

        return "".join(buffer)

class SolutionB:  # 33 ms
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from io import StringIO

        longest = word1 if len(word1) >= len(word2) else word2
        shortest = word2 if longest == word1 else word1

        buffer = StringIO()

        for i, j in zip(word1, word2):
            buffer.write(i + j)

        buffer.write(longest[len(shortest):])

        value = buffer.getvalue()
        buffer.close()

        return value

class SolutionC:  # 25 ms
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from io import StringIO

        longest = word1 if len(word1) >= len(word2) else word2
        shortest = word2 if longest == word1 else word1

        buffer = StringIO()

        for i, j in zip(word1, word2):
            buffer.write(i)
            buffer.write(j)

        buffer.write(longest[len(shortest):])

        value = buffer.getvalue()
        buffer.close()

        return value

