import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []

        for i in nums:
            heapq.heappush(hp, i)
            if len(hp) > k:
                heapq.heappop(hp)
        
        
        return hp[0]

            
        