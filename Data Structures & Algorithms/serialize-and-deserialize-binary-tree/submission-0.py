# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.values = [] 

        def traverse(node):
            if not node:
                self.values.append("#")
                return
            
            self.values.append(str(node.val))

            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return ','.join(self.values)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        dq = collections.deque(data.split(","))

        def makeTree():
            nodeval = None
            if dq:
                nodeval = dq.popleft()
            else:
                return 
            
            if nodeval!= "#":
                tn = TreeNode(int(nodeval))
                tn.left = makeTree()
                tn.right = makeTree()

                return tn 

            else:
                return None
        
        return makeTree()
