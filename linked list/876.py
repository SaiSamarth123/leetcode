# 876. Middle of the Linked List

# Easy

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast is not None and fast.next is not None:

            fast = fast.next.next
            slow = slow.next

        return slow
