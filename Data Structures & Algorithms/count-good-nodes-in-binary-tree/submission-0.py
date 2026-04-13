# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0

        def findPaths(node, max_seen):
            if not node:
                return 
            
            if node.val >= max_seen:
                self.output+=1
                max_seen = node.val
            
            findPaths(node.left, max_seen)
            findPaths(node.right, max_seen)
        
        findPaths(root, float("-inf"))

        return self.output
        