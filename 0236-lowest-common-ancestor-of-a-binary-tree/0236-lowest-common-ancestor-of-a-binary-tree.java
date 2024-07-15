/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return root;
        if(root==p || root == q) return root;
        boolean res1 = canFind(root.left,p);
        boolean res2 = canFind(root.right,q);
        if((res1 && res2) || (!res1 && !res2)) return root;
        if(!res1 && res2) return lowestCommonAncestor(root.right,p,q);
        if(res1 && !res2) return lowestCommonAncestor(root.left,p,q);
        return root;
    }

    public boolean canFind(TreeNode root, TreeNode toFind){
        if(root == null) return false;
        if(root == toFind) return true;
        return canFind(root.left,toFind) || canFind(root.right,toFind);
    }
}