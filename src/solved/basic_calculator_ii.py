"""https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its
value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will
be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as
mathematical expressions, such as eval().

# Examples

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5

# Constraints

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of
spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    """
    Notes:
        - No `eval()`
        - Integer divisions -> math.floor(i/j)
        - Expressions always valid
        - Multiplications & division -> PEMDAS priority

    Questions:
        - Elements always integers?
        - What operators? parenthesis?

    Some examples:
        - "3+2*2"
        - " 3/2"
        - " 3+534 / 2"
        - "0 * 1 + 2"

        - " 0 * 3 *2 / 3 -+ 1
        - " +3 * 3 - 2

        x " -3 + 2 * 4"
        x " 4 + 5 -"
    """
    def calculate(self, s: str) -> int:
        import math

        from typing import Tuple

        def next_number(expression: int) -> Tuple[int, str]:
            partial_number: str = ""

            for i, s in enumerate(expression):

                if not partial_number:
                    if not partial_number and s in "+-":  # ignore preceding sum and minus
                        continue
                    elif not partial_number and s in "+/":  # invalid expression
                        raise ValueError("Invalid expression %s" % expression)
                    else:
                        partial_number = s
                        continue

                if s in "+-*/":
                    break
                else:
                    partial_number += s

            remaining_expression = "" if i == len(expression) - 1 else expression[i:]
            return int(partial_number), remaining_expression

        def resolve(expression: str) -> int:
            # print(f"resolve {expression}")
            total, remaining_expression = next_number(expression)

            while remaining_expression:
                operator = remaining_expression[0]
                number, remaining_expression = next_number(remaining_expression[1:])
                match operator:
                    case "*":
                        total = total * number
                    case "/":
                        total = math.floor(total / number)
            # print(f"return {total}")
            return total

        s = s.replace(" ", "")
        total = 0
        for add_expression in s.split("+"):
            subtract_expressions = add_expression.split("-")
            total += resolve(subtract_expressions[0])
            for expression in subtract_expressions[1:]:
                total -= resolve(expression)
        return total


