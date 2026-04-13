class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for i in prerequisites:
            adj_list[i[0]].append(i[1])
        
        state = [0] * numCourses
        lst = []
        not_visited, visiting, visited = 0,1,2
        
        def dfs(node):
            if state[node] == visiting: return False

            if state[node] == visited: return True

            state[node] = visiting


            for nei in adj_list[node]:
                 if not dfs(nei): return False

            state[node] = visited
            lst.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return lst
        