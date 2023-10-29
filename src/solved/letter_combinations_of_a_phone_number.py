"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note
that 1 does not map to any letters.

# Examples

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

# Constraints

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = digits.replace("1", "")

        if len(digits) == 0:
            return []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        for d in digits:
            new_combinations = [] if combinations else list(digit_map[d])

            for letter in digit_map[d]:
                new_combinations.extend(comb + letter for comb in combinations)

            combinations = new_combinations

        return combinations
