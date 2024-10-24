from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], d: int):
        if root is None:
            return ""
        result = f"{d}{root.val}"

        if root.left is None:
            return result + self.dfs(root.right, d + 1)

        if root.right is None:
            return result + self.dfs(root.left, d + 1)

        if root.left.val < root.right.val:
            return result + self.dfs(root.left, d + 1) + self.dfs(root.right, d + 1)

        return result + self.dfs(root.right, d + 1) + self.dfs(root.left, d + 1)

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1 = self.dfs(root1, 0)
        r2 = self.dfs(root2, 0)
        return r1 == r2