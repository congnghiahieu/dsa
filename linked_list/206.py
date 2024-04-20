# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse linked list iteratively
        prev_node = next_node = None

        while head != None:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node

    def reverseList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse linked list recursively
        """To be continue"""
