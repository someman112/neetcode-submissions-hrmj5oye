# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if type(p) != type(q):
                return False
            
            if type(p) == type(q) and p is None:
                return True
            
            elif type(p) == type(q):
                return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            if node and node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            if node:
                dq.append(node.left)
                dq.append(node.right)
        
        return False
        