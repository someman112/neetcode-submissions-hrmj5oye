class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        output = [-1.0] * len(queries)
        adj=defaultdict(dict)
        for i in range(len(equations)):
            n,d = equations[i][0], equations[i][1]
            adj[n][d] = values[i]
            adj[d][n] = 1 / values[i]
        

        def dfs(node, target, visited, i, val):
            if node in visited: return 
            visited.add(node)

            for nei in adj[node]:
                if nei == target:
                    output[i] = adj[node][nei] * val
                    return
                
                dfs(nei, target, visited, i, adj[node][nei] * val)

        
        for i in range(len(queries)):
            n,t = queries[i][0], queries[i][1]

            dfs(n, t, set(), i, 1.0)
        
        return output



        
        