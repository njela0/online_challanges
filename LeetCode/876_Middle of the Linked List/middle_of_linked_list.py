# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """returns the middle node of the linked list"""
        count = 0
        current_node = head

        while current_node:
            count += 1
            current_node = current_node.next

        middle_node_index = count // 2
        current_node = head

        for _ in range(middle_node_index):
            current_node = current_node.next

        return current_node

# example for linked list 1 -> 2 -> 3 -> 4 -> 5
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

sol1 = Solution()
print("middle node head1:", sol1.middleNode(head1).val)


def build_linked_list(values):
    """Function to build a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

head2 = build_linked_list([1, 2, 3, 4, 5, 6])

sol2 = Solution()
print("middle node head2:", sol2.middleNode(head2).val)
