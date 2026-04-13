class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for i in range(len(points)):
            a,b = points[i]

            for j in range(i+1, len(points)):
                x,y = points[j]
                dist = abs(a-x)+abs(b-y)
                adj_list[i].append((dist, j))
                adj_list[j].append((dist, i))
        
        visited = set()
        hp = [(0,0)]
        res = 0

        while len(visited) != len(points):
            dist, node = heapq.heappop(hp)

            if node in visited:
                continue 
            
            res+=dist 
            visited.add(node)

            for nei_dist, nei in adj_list[node]:
                
                if nei not in visited:
                    heapq.heappush(hp, (nei_dist, nei))
        
        return res
        