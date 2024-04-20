# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Move slow pointer to middle using fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse linked list from middle (from slow)
        prev_node = next_node = None
        while slow != None:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        # Reset fast to head of linked list, slow to tail of linkest list
        # Note that after reverse linked list, prev_node point to tail, slow point to None
        fast, slow = head, prev_node

        # Check two pointer (one at head, one at tail) if is palindromed
        while fast != None and slow != None:
            if fast.val != slow.val:
                return False

            fast, slow = fast.next, slow.next

        return True
