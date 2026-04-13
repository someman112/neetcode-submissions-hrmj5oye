# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def levelOrder(root):
            dq = deque()
            dq.append(root)
            output = []

            while True:
                nodes = []
                
                while dq:
                    n = dq.popleft()
                    if n:
                        nodes.append(n)
                
                for n in nodes:
                    dq.append(n.left)
                    dq.append(n.right)
                
                if not dq:
                    break
                else:
                    output.append([n.val for n in nodes])

            return output

        lvl_order = levelOrder(root)
        return [lst[-1] for lst in lvl_order]
        