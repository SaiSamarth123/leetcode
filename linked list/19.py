# 19. Remove Nth Node From End of List

# Medium
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # curr = head
        # length = 0

        # while curr:
        #     length = length + 1
        #     curr = curr.next

        # target = length - n - 1
        # prev = head
        # curr = prev.next

        # if target is -1:
        #     head = head.next

        # while curr:
        #     if target is 0:
        #         prev.next = curr.next
        #     target = target - 1
        #     prev = curr
        #     curr = curr.next

        # return head
        dummy = ListNode(0)
        dummy.next = head

        first, second = dummy, dummy

        for i in range(n):
            second = second.next

        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next
