"""https://leetcode.com/problems/group-shifted-strings/

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence:
"abc" -> "bcd" -> ... -> "xyz".

Given an array of strings, group all strings[i] that belong to the same shifting
sequence. You may return the answer in any order.

# Examples

Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]

# Constraints

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    """
    A few notes:

    1. For any string, any shift will preserve the integer difference between consecutive letters
    2. We can shift any string until we start with a. Difference secuence is preserved as all letters are shifted the same steps.
    3. Any string in the same group should now have the same form.

    Shift ammount: difference from first element to 'a'. If '', ammount is 0.
    Shift all others by same ammount

    '' | 0 | ''
    'a' | 0 | 'a'
    'ab' | 0 | 'ab'
    'aaaccasd' | 0 | 'aaaccasd'
    'bas' | 1 | 'azr'

    Keep dict of normalized string to list of original strings. Return as list.

    Complexity: O( len(strings[i]) )
    """

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        import string as python_string

        from collections import defaultdict

        alphabet: str = python_string.ascii_lowercase

        def shift_letter(letter: str, shift_amount: int) -> str:
            try:
                shifted_index = alphabet.index(letter) - shift_amount
                return alphabet[shifted_index]
            except ValueError as e:
                raise ValueError(
                    "shift_letter by %s failed for %s" % (shift_amount, letter)
                ) from e

        def normalize(string: str) -> str:
            shift_amount = alphabet.index(string[0])
            shifted_letters = [shift_letter(letter, shift_amount) for letter in string]
            return "".join(shifted_letters)

        groups = defaultdict(list[str])

        for string in strings:
            normalized = normalize(string)
            groups[normalized].append(string)

        return list(groups.values())
