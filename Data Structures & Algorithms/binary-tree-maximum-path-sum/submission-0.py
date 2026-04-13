# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def recurse(node):
            if node == None:
                return 0
        
            left = max(0, recurse(node.left))
            right = max(0, recurse(node.right))

            split = node.val + left + right
            non_split = node.val + max(left, right)

            self.ans = max(self.ans, max(split, non_split))

            return non_split
        
        recurse(root)
        return self.ans
        