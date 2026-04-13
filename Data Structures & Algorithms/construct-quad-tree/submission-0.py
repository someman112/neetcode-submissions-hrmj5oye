"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            leaf=True

            for i in range(n):
                for j in range(n):
                    if grid[r+i][c+j]!=grid[r][c]:
                        leaf=False
                        break
                if not leaf: break
            
            if leaf: return Node(grid[r][c], True)

            n=n//2
            tl, tr = dfs(n, r, c),  dfs(n, r, c+n)
            bl, br = dfs(n, r+n,c), dfs(n, r+n, c+n)
            return Node(grid[r][c], False, tl,tr,bl,br)
        
        return dfs(len(grid), 0,0)