# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.helper(root)
    
    def helper(self,root):
        if not root:
            return None
        left_tail = self.helper(root.left)
        right_tail = self.helper(root.right)
        # if root.left and root.right:
        #     root.right = root.left
        #     right.next = root.right
        #     root.left = None
        # elif not root.left:
        #     root.right = root.left
        #     root.left = None
        if root.left :
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail or left_tail or root