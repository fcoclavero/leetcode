"""https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the
array.

Note that it is the kth largest element in the sorted order, not the kth distinct
element.

Can you solve it without sorting?

# Example

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

# Constraints

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    """
    nums -> not necessarily sorted
    no sorting -> less than n log n time

    - aux = []
    - for n in nums
        - compare n with aux[0] -> edge case for empty list
            - if larger, insert n, remove first element if len(aux) = k
            - else, continue
    - return aux[-k]

    complexity:
        - iterative insert: O(n*k) <= O(n^2)
        - binray search insert: O(n*log(k)) <= O(n*log(n))

    edge cases:
        - empty list
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        if not nums:
            return None

        min_heap = []
        for n in nums:  # 1
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                if n > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, n)

        return min_heap[0]
