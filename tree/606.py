# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self._tree2str(root)

    def _tree2str(self, node: Optional[TreeNode]) -> str:
        if node == None:
            return ""

        ans = str(node.val)

        if node.left != None:
            ans += f"({self._tree2str(node.left)})"

        if node.right != None:
            if node.left == None:
                ans += "()"
            ans += f"({self._tree2str(node.right)})"

        return ans
