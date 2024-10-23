# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            cur