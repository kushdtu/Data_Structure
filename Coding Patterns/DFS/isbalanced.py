# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return (max(left, right) + 1)
        
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return (self.isBalanced(root.left) and self.isBalanced(root.right) \
                 and abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1)