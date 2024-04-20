# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.carry = 0

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None

        sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + self.carry
        self.carry = sum // 10
        node_val = sum % 10

        node = ListNode(node_val)

        if (
            (l1 == None or l1.next == None)
            and (l2 == None or l2.next == None)
            and self.carry
        ):
            node.next = ListNode(self.carry)
        else:
            node.next = self.addTwoNumbers(
                l1.next if l1 else None, l2.next if l2 else None
            )

        return node
