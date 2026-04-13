from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited: return

            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei)
        
        num_components = 0
        idx = 0

        while idx < n:
            if idx not in visited:
                dfs(idx)
                num_components+=1
            
            idx+=1 
        
        return num_components





        
        