# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    toRet = TreeNode()
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.helper(root, p, q)
        return self.toRet
    
    def helper(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not root: return False

        l = self.helper(root.left, p, q)
        r = self.helper(root.right, p, q)

        if l and r:
            self.toRet = root
        
        if (l or r) and (root.val == p.val or root.val == q.val):
            self.toRet = root
        
        return l or r or root == p or root == q



        
