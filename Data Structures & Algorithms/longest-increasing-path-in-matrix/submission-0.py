class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]
        ans = -1

        def dfs(i,j):            
            if cache[i][j] != 0:
                return cache[i][j]

            nonlocal ans
            res = 0
            for x,y in [(0,1), (1,0), (-1,0), (0,-1)]:
                ix, jy = i+x, j+y
                
                if 0<=ix<m and 0<=jy<n and matrix[ix][jy] > matrix[i][j]:
                    res = max(res, dfs(ix, jy))
            
            cache[i][j] = 1 + res
            ans = max(cache[i][j], ans)

            return cache[i][j]


        for i in range(m):
            for j in range(n):
                dfs(i,j)

        return ans
        