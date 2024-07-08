# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.hash = {}
        self.l=[]
        def helper(root,level):
            if not root:
                return
            if level not in self.hash:
                self.l.append(root.val)
                self.hash[level] = root.val
            helper(root.right,level+1)
            helper(root.left,level+1)
        helper(root,0)
        return self.l