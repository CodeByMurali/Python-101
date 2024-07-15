"""
https://leetcode.com/problems/design-linked-list/description/
"""


class ListNode:
    # Create a node class
    def __init__(self, val) -> None:
        # The node has a value
        self.val = val
        # Next pointer
        self.next = None
        # Previous pointer
        self.prev = None


class MyLinkedList:

    # Function to initialize a new linked list
    def __init__(self):
        # Create dummy left and right nodes to avoid edge cases
        self.left = ListNode(0)
        self.right = ListNode(0)

        # Set pointers for these dummy nodes
        self.left.next = self.right
        self.right.prev = self.left

    # Algorithm for getting the value of a node at a specific index
    """
    Traversing: 
    Start with the node next to the left dummy node
    Iterate until we reach the required node
    Return the value of the node at the given index

    Edge cases:
    Return -1 if we are at one of the dummy nodes 
    If the index does not become 0, it implies the linked list is too short    
    """

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        # At this point we have reached the node for the given index
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    # Algorithm for adding a node at the head
    """
    Create a new node
    Add the new node next to the left dummy node
    Update the pointers accordingly
    """

    def addAtHead(self, val: int) -> None:
        prev, node, next = self.left, ListNode(val), self.left.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    # Algorithm for adding a node at the tail
    """
    Create a new node
    Add the new node before the right dummy node
    Update the pointers accordingly
    """

    def addAtTail(self, val: int) -> None:
        prev, node, next = self.right.prev, ListNode(val), self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    # Algorithm for adding a node at a specific index
    """
    Start with the node after the left dummy node
    Traverse until the index
    Perform the same edge case checks as get
    It is valid to insert at the position of the right dummy node
    """

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        # Traverse to the index
        while curr and index > 0:
            curr = curr.next
            index -= 1
        # At this point we have reached the node for the given index
        if curr and index == 0:
            prev, node, next = curr.prev, ListNode(val), curr
            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    # Algorithm for deleting a node at a specific index
    """
    Start with the node after the left dummy node
    Traverse until the index
    Perform the same edge case checks as get
    Instead of creating a new node, update the pointers to remove the node
    """

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        # Traverse to the index
        while curr and index > 0:
            curr = curr.next
            index -= 1
        # At this point we have reached the node for the given index
        if curr and index == 0 and curr != self.right:
            prev, next = curr.prev, curr.next
            prev.next = next
            next.prev = prev


# Dummy invocation for all methods
my_linked_list = MyLinkedList()
my_linked_list.addAtHead(1)
my_linked_list.addAtTail(3)
my_linked_list.addAtIndex(1, 2)    # linked list becomes 1->2->3
print(my_linked_list.get(1))       # return 2
my_linked_list.deleteAtIndex(1)    # now the linked list is 1->3
print(my_linked_list.get(1))       # return 3
