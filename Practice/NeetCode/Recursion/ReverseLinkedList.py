# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the Solution class with the reverseList method


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Base case: if the list is empty or has only one node, return the head
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)

        # Reverse the current node's next pointer
        head.next.next = head
        head.next = None

        # Return the new head of the reversed list
        return new_head

# Helper function to create a linked list from a list of values


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list of values


def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


# Create a linked list from a list of values
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

# Instantiate the Solution class
solution = Solution()

# Call the reverseList method and get the reversed linked list
reversed_head = solution.reverseList(head)

# Convert the reversed linked list back to a list of values
reversed_values = linked_list_to_list(reversed_head)
reversed_values
