from functools import lru_cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary=set(dictionary)
        n=len(s)

        @lru_cache
        def dfs(i):
            if i==n: return 0

            res=1+dfs(i+1)

            for w in dictionary:
                wl = len(w)
                if i+wl<=n and s[i:i+wl]==w:
                    res=min(res, dfs(i+wl))
            
            return res
        
        return dfs(0)
        