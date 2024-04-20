# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        left_node, prev_left_node = head, None
        til_left, til_right = left, right - left

        # Get left_node to position
        while left_node != None and til_left > 1:
            prev_left_node = left_node
            left_node = left_node.next
            til_left -= 1

        # Reverse from left_node to right_node
        prev_right_node = next_right_node = None
        right_node = left_node
        while right_node != None and til_right >= 0:
            next_right_node = right_node.next
            right_node.next = prev_right_node
            prev_right_node = right_node
            right_node = next_right_node
            til_right -= 1

        # Reverse 2 head of left node and right node
        # Input: head = [1,2,3,4,5], left = 2, right = 4
        # Output: [1,4,3,2,5]
        # til_left = 2, til_right = 2
        # left_node = 2, prev_left_node = 1
        # After reverse from left_node to right_node step, we get these:
        # 1. right_node = 5, prev_right_node = 4
        # 2. 1 -> 2 <- 3 <- 4 -> 5
        # Output we want: 1 -> 4 -> 3 -> 2 -> 5
        if prev_left_node != None:
            prev_left_node.next = prev_right_node
        else:
            # if not prev_left_node, left_node is head. So head must point to prev_right_node
            head = prev_right_node

        if left_node != None:
            left_node.next = right_node

        return head
