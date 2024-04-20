# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.prev_node: Optional[TreeNode] = None
        self.min_diff = 999_999

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return self.min_diff

        self.minDiffInBST(root.left)
        if self.prev_node != None:
            self.min_diff = min(self.min_diff, abs(root.val - self.prev_node.val))
        self.prev_node = root
        self.minDiffInBST(root.right)

        return self.min_diff
