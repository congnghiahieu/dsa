# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)

    def dfs(self, node: Optional[TreeNode], current_sum: int, targetSum: int) -> bool:
        if node == None:
            return False

        current_sum += node.val

        if node.left == None and node.right == None:
            return current_sum == targetSum

        for child_node in [node.left, node.right]:
            if child_node != None and self.dfs(child_node, current_sum, targetSum):
                return True

        return False
