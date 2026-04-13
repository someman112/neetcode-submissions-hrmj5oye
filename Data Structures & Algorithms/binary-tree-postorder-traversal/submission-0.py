# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, ans = [], []
        curr = root
        last_visited = None
        

        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            

            if stack[-1].right and last_visited!= stack[-1].right:
                curr = stack[-1].right
            
            else:
                last_visited = stack.pop()
                ans.append(last_visited.val)
        
        return ans 
        

        