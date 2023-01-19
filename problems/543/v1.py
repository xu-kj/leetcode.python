from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
            self.depthOfBinaryTree(root.left) + self.depthOfBinaryTree(root.right))

    def depthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.depthOfBinaryTree(root.left), self.depthOfBinaryTree(root.right)) + 1
