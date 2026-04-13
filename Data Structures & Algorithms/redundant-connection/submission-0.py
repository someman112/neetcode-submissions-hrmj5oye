from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [-1] * (len(edges)+1)

        def abs_root(node):
            ans = node
            while root[ans] != -1:
                ans = root[ans]
            return ans

        def union(a, b):
            root[abs_root(a)] = abs_root(b)


        ans = None
        for e, v in edges:
            if abs_root(e) == abs_root(v):
                ans = [e,v]
            else:
                union(e,v)
        
        return ans
        
        

        

        