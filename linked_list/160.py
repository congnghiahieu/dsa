# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None

        node_a, node_b = headA, headB

        while node_a != node_b:
            node_a = node_a.next if node_a != None else headB
            node_b = node_b.next if node_b != None else headA

        return node_a
