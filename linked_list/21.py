# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dump_head_node = ListNode()
        current_node = dump_head_node

        while list1 != None or list2 != None:
            if list1 == None or list2 == None:
                current_node.next = list2 if list1 == None else list1
                break

            if list1.val <= list2.val:
                current_node.next = list1
                current_node, list1 = current_node.next, list1.next
            else:
                current_node.next = list2
                current_node, list2 = current_node.next, list2.next
        return dump_head_node.next
