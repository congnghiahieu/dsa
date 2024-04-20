# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        low, fast = [head] * 2
        while low != None and fast != None:
            low, fast = low.next, fast.next
            if low == None or fast == None:
                return False
            fast = fast.next
            if low == fast:
                return True

        return False
