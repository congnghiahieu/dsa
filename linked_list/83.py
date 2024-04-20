# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node, prev_node = head, None
        while current_node != None:
            if prev_node and current_node.val == prev_node.val:
                prev_node.next, current_node = [current_node.next] * 2
            else:
                prev_node = current_node
                current_node = current_node.next

        return head
