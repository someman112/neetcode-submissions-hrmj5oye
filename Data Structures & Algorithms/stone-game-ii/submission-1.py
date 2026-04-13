from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp = {}
        
        @lru_cache(None)
        def dfs(i, m, turn):
            if i==len(piles): return 0
            
            if turn==0:
                val = 0
                res=0
                for x in range(1, min(n-i, 2*m)+1):
                    val+=piles[i+x-1]
                    res = max(res, val + dfs(i+x, max(m,x), 1))

                return res
            
            #bobs turn leads to minimal stones for alice
            val=0
            res = float("inf")
            for x in range(1, min(n-i, 2*m)+1):
                res = min(res, dfs(i+x, max(m,x), 0))
            
            return res
        
        return dfs(0, 1, 0)