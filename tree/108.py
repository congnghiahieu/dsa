# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        root = self._sortedArrayToBST(nums, 0, len(nums) - 1)
        return root

    def _sortedArrayToBST(self, nums: list[int], l: int, h: int) -> Optional[TreeNode]:
        if l > h:
            return None

        m = ((h - l) // 2) + l
        mid_node = TreeNode(nums[m])
        mid_node.left = self._sortedArrayToBST(nums, l, m - 1)
        mid_node.right = self._sortedArrayToBST(nums, m + 1, h)

        return mid_node
