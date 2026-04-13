class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        cost.append(0)

        ans = float("inf")
        for i in range(n-1, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
            
        
        return min(cost[0], cost[1])
        