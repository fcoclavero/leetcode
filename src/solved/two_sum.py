"""https://leetcode.com/problems/two-sum/

# Problem

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.

# Examples

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

# Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

> Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
from typing import List


class Solution:
    """
    Examples:

    [1, 3, 5]  x=8  -> [1, 2]
    [1, 3, 6]  x=8  -> []
    [9, 3, 3, 2, 5]  x=8 -> [1, 4]
    [4, 3, 3, 2, 5]  x=8 -> [1, 4]
    [9, 3, 3, 2, 5, -1] x=8 -> [0, 5]
    [-2, -1, 5, -3, 5] x=-3 -> [0, 1]

    Assume:

    len(nums) >= 2
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        diffs = defaultdict(list)  # {}

        for i, num in enumerate(nums):  # 0, 1
            diff = target - num  # 4, 5
            # {4: 0}, {4: 0, 5: 1}, ..., {4: [0], 5: [1,2], 6: [3], 3: [4]}
            diffs[diff].append(i)

        for i, num in enumerate(nums):  # 0, 1 ...
            if diffs[num]:
                if i != diffs[num][0]:
                    return [i, diffs[num][0]]
                elif len(diffs[num]) > 1:
                    return [i, diffs[num][1]]

        return []
