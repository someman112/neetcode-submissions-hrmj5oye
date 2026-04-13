import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1

        heapq.heapify(stones)
        while len(stones) > 1:
            max1 = heapq.heappop(stones) * -1
            max2 = heapq.heappop(stones) * -1

            if max1 > max2:
                heapq.heappush(stones, (max1 - max2) * -1)
        
        if stones:
            return stones[0] * -1 
        
        return 0
        