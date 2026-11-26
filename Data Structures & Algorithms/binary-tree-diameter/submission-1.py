# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd=0
        self.diameterHelper(root)
        return self.maxd
    
    def diameterHelper(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        lmax=self.diameterHelper(root.left)
        rmax=self.diameterHelper(root.right)
        self.maxd=max(self.maxd, lmax+rmax)
        return 1+max(lmax, rmax)