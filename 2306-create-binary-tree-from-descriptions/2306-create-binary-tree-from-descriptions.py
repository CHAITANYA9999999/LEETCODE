# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        isparents={}
        graph = {}

        for parent,child,isLeft in descriptions:
            if parent not in graph:
                graph[parent] = TreeNode(parent)
            if child not in graph:
                graph[child] = TreeNode(child)
            if isLeft:
                graph[parent].left = graph[child]
            else:
                graph[parent].right = graph[child]
            isparents[child] = True
            if parent not in isparents:
                isparents[parent] = False
            
        
        print(isparents)
        for key,value in isparents.items():
            if not value:
                return graph[key]