#  Definition for a binary tree node.
from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        res = []
        q = Queue()
        q.put_nowait([root])

        while not q.empty():
            node = q.get_nowait()
            res.append(node.val)

            if node.left:
                q.put_nowait(node.left)
            if node.right:
                q.put_nowait(node.right)

        return res
