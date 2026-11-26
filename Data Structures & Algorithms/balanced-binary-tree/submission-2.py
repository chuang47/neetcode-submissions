# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance=True
        self.height(root)
        return self.balance
    
    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        if abs(lh-rh) > 1:
            self.balance = False
        
        return 1+max(lh,rh)