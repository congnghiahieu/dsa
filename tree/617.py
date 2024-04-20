# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        root = self._mergeTrees(root1, root2)
        return root

    def _mergeTrees(
        self, node1: Optional[TreeNode], node2: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        if node1 == None and node2 == None:
            return None

        merged_node = TreeNode(
            (node1.val if node1 != None else 0) + (node2.val if node2 != None else 0)
        )

        merged_node.left = self._mergeTrees(
            node1.left if node1 != None else None,
            node2.left if node2 != None else None,
        )
        merged_node.right = self._mergeTrees(
            node1.right if node1 != None else None,
            node2.right if node2 != None else None,
        )

        return merged_node
