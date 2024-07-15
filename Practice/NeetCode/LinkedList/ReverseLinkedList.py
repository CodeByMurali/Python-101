# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            # Take a backup of the next node before altering the nodes
            nxt = curr.next
            # Make the next pointer point to the previuos node
            curr.next = prev
            # Move left so that the previous node becomes the new current node
            prev = curr
            # Repeat the process to the next node
            curr = nxt
        return prev
