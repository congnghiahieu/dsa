#  Definition for singly-linked list.
from math import ceil
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Fast and slow pointer"""
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Naive approach"""
        current_node, mid = head, ceil((self.get_length(head) + 1) / 2)
        while current_node != None and mid > 1:
            current_node, mid = current_node.next, mid - 1
        return current_node

    def get_length(self, head: Optional[ListNode]) -> int:
        current_node, length = head, 0
        while current_node != None:
            current_node, length = current_node.next, length + 1
        return length
