# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs = 0
        def dfs(node):
            if not node:
                return []  
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l+r<=distance:
                        self.pairs +=1

            total = left+right
            return [x+1 for x in total ]
        
        dfs(root)
        return self.pairs