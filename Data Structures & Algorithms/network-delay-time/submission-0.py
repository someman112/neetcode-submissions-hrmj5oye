class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u,v,time in times:
            adj_list[u].append((v,time))

        min_times = {}
        hp = [(0,k)]
        t = 0

        while hp:
            dist, node = heapq.heappop(hp)
            if node in min_times:
                continue
            
            min_times[node] = dist
            t = max(t, dist)

            for nei, nei_dist in adj_list[node]:
                if nei not in min_times:
                    heapq.heappush(hp, (dist+nei_dist, nei))
                
        
        return t if len(min_times) == n else -1

        