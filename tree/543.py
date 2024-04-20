# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def get_depth(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0

        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        self.diameter = max(self.diameter, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_depth(root)
        return self.diameter
