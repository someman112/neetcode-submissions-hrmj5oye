class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        
        def dfs(l,r):
            if l > r: return 0
            if (l,r) in dp: return dp[(l,r)]

            turn = (r - l) %2 != 0 
            left_val = piles[l] if turn==0 else 0
            right_val = piles[r] if turn==0 else 0
            
            dp[(l,r)] = max(dfs(l+1, r)+left_val, dfs(l,r-1)+right_val)
            return dp[(l,r)]
        
        opt_alice =  dfs(0, len(piles)-1)
        return opt_alice > sum(piles) - opt_alice
        