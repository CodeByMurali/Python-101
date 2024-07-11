"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Initiate a dummy node to simplify insertion into an empty list
        # The head of the merged list will be the next node of this dummy node
        dummy = ListNode()

        # Start the tail at the dummy node; tail will track the end of the merged list
        tail = dummy

        # Loop until one of the lists is empty
        while list1 and list2:
            # Compare values of the current nodes of list1 and list2
            if list1.val < list2.val:
                # If list1's value is smaller, attach it to the merged list
                tail.next = list1
                # Move list1's pointer to the next node
                list1 = list1.next
            else:
                # If list2's value is smaller or equal, attach it to the merged list
                tail.next = list2
                # Move list2's pointer to the next node
                list2 = list2.next
            # Move tail to the last node in the merged list
            tail = tail.next

        # At least one of the lists is now empty; attach the remaining elements
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # The merged list is next to the dummy node
        return dummy.next
