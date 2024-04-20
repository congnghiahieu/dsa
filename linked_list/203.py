# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node, prev_node = head, None
        while current_node != None:
            if current_node.val != val:
                prev_node = current_node
                current_node = current_node.next
                continue

            if current_node == head:
                head, current_node = [head.next] * 2
            else:
                prev_node.next = current_node.next
                current_node = current_node.next

        return head
