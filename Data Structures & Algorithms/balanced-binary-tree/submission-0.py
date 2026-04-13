# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: TreeNode) -> int:
            if not node:
                return 0
            lh = height(node.left)
            if lh < 0:           
                return -1
            rh = height(node.right)
            if rh < 0:           
                return -1
            if abs(lh - rh) > 1: 
                return -1
            return max(lh, rh) + 1
        
        return height(root) >= 0
        