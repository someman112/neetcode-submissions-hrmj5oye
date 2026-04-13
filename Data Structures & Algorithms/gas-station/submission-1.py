class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res, tank, total = 0, 0, 0


        for i in range(len(gas)):

            total+= gas[i] - cost[i]  
            tank+= gas[i] - cost[i]

            if tank < 0:
                res = i + 1
                tank = 0
            
        return res if total>=0 else -1

        