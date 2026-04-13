# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findPath(tree, node):
            path = [tree]

            while tree is not None and tree.val!= node.val:
                if node.val > tree.val:
                    tree = tree.right
                
                else:
                    tree = tree.left
                
                path.append(tree)
            return path
        
        path1 = findPath(root, p)
        path2 = findPath(root, q)
        curr_common = None

        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                curr_common = path1[i]
        
        return curr_common
        