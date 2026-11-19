/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    int max=0;
    public int diameterOfBinaryTree(TreeNode root) {
        diameterHelper(root);
        return max;
    }

    private int diameterHelper(TreeNode root){
        if(root==null){
            return 0;
        }

        int left=diameterHelper(root.left);
        int right=diameterHelper(root.right);
        max=Math.max(max, left+right);
        return 1+Math.max(left, right);


    }
}
