class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res = {}
        hp = []
        i = 0


        for q in sorted(queries):
            
            while i < len(intervals) and intervals[i][0] <= q:
                li = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(hp, (li, intervals[i][1]))
                i+=1
            
            while hp and hp[0][1] < q:
                heapq.heappop(hp)
            
            res[q] = hp[0][0] if hp else -1 

        
        return [res[q] for q in queries]
        