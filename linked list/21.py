# Merge two sorted linked list
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # head = ListNode(0)
        # curr3 = head

        # while list1 and list2:

        #     if list1.val <= list2.val:
        #         curr3.next = list1
        #         list1 = list1.next
        #     else:
        #         curr3.next = list2
        #         list2 = list2.next
        #     curr3 = curr3.next
        # if list1:
        #     curr3.next = list1
        # else:
        #     curr3.next = list2

        # return head.next

        # Recursive solution
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
