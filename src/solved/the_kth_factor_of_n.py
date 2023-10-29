"""https://leetcode.com/problems/the-kth-factor-of-n/

You are given two positive integers n and k. A factor of an integer n is defined as an
integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in
this list or return -1 if n has less than k factors.

# Examples

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

# Constraints

1 <= k <= n <= 1000
"""


class Solution:
    """
    Notes:
        - Brute force solution: create range(n) -> iterate -> keep counter of factors
            -> return kth => O(n)
        - 1 and n are always in the factor list -> len(factors) >= 2

    [1,2,4,8,16]
    [1,2,3,6,9,18]
    """

    def kthFactor(self, n: int, k: int) -> int:
        # Brute force:

        # factors = 0
        # for i in range(1, n + 1):
        #     if n % i == 0:
        #         factors += 1
        #         if factors == k:
        #             return i
        # return -1

        # - less than O(n) hints at log(n)
        # - this hints a binary-search-like algorithm
        # - we can take advantage of the modulus operator to get to the nearest factor
        #   to the left of a current number
        # - factor list is uneven when n % k == 0 and n / k = k

        if n == 1 and k > 1:
            return -1

        if k == 1:
            return 1

        factors_lower = [1]
        factors_upper = [n]
        factor = 2

        while factor < factors_upper[-1]:  # iterates at most sqrt.(n) times
            if n % factor == 0:
                factors_lower.append(factor)
                factors_upper.append(int(n / factor))

                if len(factors_lower) >= k:
                    return factors_lower[k - 1]

            factor += 1

        if factors_lower[-1] == factors_upper[-1]:  # remove duplicate factor
            factors_upper.pop()

        if len(factors_lower) + len(factors_upper) < k:
            return -1

        return factors_upper[-(k - len(factors_lower))]
