from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        not_visited, visiting, visited = 0,1,2
        if len(edges) != n-1: return False

        adj_list = defaultdict(list)
        for i in edges:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])

        states = [0] * n
        
        def dfs(node, parent):
            if states[node] == visiting: return False
            if states[node] == visited: return True

            states[node] = visiting

            for nei in adj_list[node]:
                if nei!= parent and not dfs(nei, node): return False

            states[node] = visited

            return True 
        

        return dfs(0, None) and all(states[i] == visited for i in range(n))




        
        