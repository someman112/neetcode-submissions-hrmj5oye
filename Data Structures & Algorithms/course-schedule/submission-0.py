class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        not_visited = 0
        visiting = 1
        visited = 2

        adj_list = defaultdict(list)
        for i in prerequisites:
            adj_list[i[0]].append(i[1])
        
        state = [0] * numCourses 

        def dfs(node):
            if state[node] == visiting: return False

            if state[node] == visited: return True 

            state[node] = visiting 

            for nei in adj_list[node]:
                if not dfs(nei): return False
            
            state[node] = visited

            return True
        

        for i in range(numCourses):
            if not dfs(i): return False
        
        return True 
        