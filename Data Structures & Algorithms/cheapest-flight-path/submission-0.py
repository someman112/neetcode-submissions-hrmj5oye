class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0


        for _ in range(k+1):
            costs_copy = costs.copy()

            for f,t,p in flights:

                if costs[f] == float("inf"):
                    continue
                
                costs_copy[t] = min(costs_copy[t], costs[f] + p)
            
            costs = costs_copy

        
        return costs[dst] if costs[dst]!= float("inf") else -1
        