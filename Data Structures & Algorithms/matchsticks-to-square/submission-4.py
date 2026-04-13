class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        summ = sum(matchsticks)
        if summ %4!=0: return False
        target = summ // 4 
        matchsticks.sort(reverse=True)
        sides = [0] * 4 
        def dfs(i):
            if i == len(matchsticks): return True 

            curr=matchsticks[i]
            for j in range(4):
                if sides[j] + curr <=target:
                    sides[j]+=curr
                    if dfs(i+1): return True
                    sides[j]-=curr
                
                if sides[j] == 0: break 
                
            return False
        
        return dfs(0)

        
        