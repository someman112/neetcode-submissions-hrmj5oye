# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def maxDepth(node):            
            if not node:
                return 0
            
            hl = maxDepth(node.left)
            hr = maxDepth(node.right)

            self.diameter = max(self.diameter, hl + hr)

            return max(hl, hr) + 1
        
        maxDepth(root)

        return self.diameter
        