# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(
        self, node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> bool:
        if node1 == None and node2 == None:
            return True

        if node1 == None or node2 == None or node1.val != node2.val:
            return False

        return self._isSymmetric(node1.left, node2.right) and self._isSymmetric(
            node1.right, node2.left
        )
