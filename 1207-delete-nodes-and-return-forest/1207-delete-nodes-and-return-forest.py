# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        q = []
        q.append(root)
        if root.val not in to_delete:
            res.append(root)

        while len(q)!=0:
            cur = q.pop(0)
            if cur.left != None:
                q.append(cur.left)
                if cur.left.val in to_delete:
                    cur.left = None
            
            if cur.right != None:
                q.append(cur.right)
                if cur.right.val in to_delete:
                    cur.right = None
            
            if cur.val in to_delete:
                if cur.left!=None:
                    res.append(cur.left)
                if cur.right != None:
                    res.append(cur.right)
                cur.left = None
                cur.right = None
        return res