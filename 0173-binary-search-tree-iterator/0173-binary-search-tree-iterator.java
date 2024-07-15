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
class BSTIterator {
    ArrayList<TreeNode> arr;
    int pointer;
    int max_pointer;
    public BSTIterator(TreeNode root) {
        arr = new ArrayList<>();
        arr.add(new TreeNode(0));
        inorder(root);
        pointer = 0;
        max_pointer = arr.size();
    }

    public void inorder(TreeNode root){
        if(root==null) return;
        inorder(root.left);
        arr.add(root);
        inorder(root.right);
    }
    
    public int next() {
        pointer++;
        return arr.get(pointer).val;
    }
    
    public boolean hasNext() {
        return pointer<max_pointer-1;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */