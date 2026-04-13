# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        
        tree = TreeNode(preorder[0]) 
        len_left = 0
        while len_left < len(inorder) and inorder[len_left] != tree.val:
            len_left+=1
        
        tree.left = self.buildTree(preorder[1:len_left+1], inorder[0:len_left])
        tree.right = self.buildTree(preorder[len_left+1:], inorder[len_left+1:])

        return tree
        
        