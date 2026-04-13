class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []

        for x,y in points:
            dist = math.sqrt((x)**2 + (y)**2) * -1
            val = (dist, [x,y])

            if len(hp) < k:
                heapq.heappush(hp, val)
            
            elif len(hp) == k and hp[0][0] < val[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, val)
        
        return [val[1] for val in hp ]
        