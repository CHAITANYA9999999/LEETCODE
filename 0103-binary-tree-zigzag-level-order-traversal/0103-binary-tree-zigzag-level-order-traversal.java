import java.util.*;

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        List<List<Integer>> zigzag = new ArrayList<>();
        int level = 0;
        
        while (!q.isEmpty()) {
            int levelSize = q.size();
            List<Integer> currentLevel = new ArrayList<>();
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode cur = q.poll();
                currentLevel.add(cur.val);
                
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            
            if (level % 2 == 1) {
                Collections.reverse(currentLevel);
            }
            
            zigzag.add(currentLevel);
            level++;
        }
        
        return zigzag;
    }
}
