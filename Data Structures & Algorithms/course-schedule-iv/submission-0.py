class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        if not prerequisites: return ans 

        adj = defaultdict(list)
        for a,b in prerequisites: adj[b].append(a)
        prereqs={}

        def dfs(node):
            if node in prereqs: return prereqs[node]
            all_prereqs = set()
            for nei in adj[node]:
                all_prereqs.add(nei)
                all_prereqs|=dfs(nei)
            
            prereqs[node] = all_prereqs 
            return all_prereqs
        
        for i in range(numCourses): dfs(i)

        for i in range(len(queries)):
            p,t = queries[i][0], queries[i][1]

            ans[i] = p in prereqs[t]
        
        return ans
        
        

        
        