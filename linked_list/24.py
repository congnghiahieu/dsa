# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, cur_node = None, head

        while cur_node != None:
            if prev_node == None:
                prev_node = cur_node
            else:
                temp = cur_node.val
                cur_node.val = prev_node.val
                prev_node.val = temp
                prev_node = None

            cur_node = cur_node.next

        return head
