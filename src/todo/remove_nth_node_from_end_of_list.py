"""

Given the head of a linked list, remove the nth node from the end of the list and return
its head.

# Examples

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

# Constraints

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        nth: Optional[ListNode] = None

        traversed = 1
        current_node = head

        while current_node:
            if n == traversed:
                if nth and not prev:
                    prev = head
                    nth = nth.next
                    continue
                elif not nth:
                    nth = head
                    continue
                else:
                    nth = nth.next
                    prev = prev.next

            else:
                traversed += 1

            current_node = current_node.next

        # Now, delete nth
        if not prev:  # to delete is first elem in list
            return nth.next
        else:
            prev.next = nth.next
            return head
