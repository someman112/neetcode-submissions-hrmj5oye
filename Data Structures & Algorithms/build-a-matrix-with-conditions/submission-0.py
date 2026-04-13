class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def dfs(curr_node,adj, visited, ordering):
            if visited[curr_node]==1: return False
            if visited[curr_node]==2: return True

            visited[curr_node]=1
            for nei in adj[curr_node]:
                if not dfs(nei, adj, visited,ordering): return False

            ordering.append(curr_node)
            visited[curr_node]=2
            return True
            
        
        
        adj_row=defaultdict(set)
        adj_col=defaultdict(set)
        for e,v in rowConditions:adj_row[e].add(v)
        for e,v in colConditions:adj_col[e].add(v)

        # cycle detection for both row and col condts
        # 0 not visted, 1 visiting, 2 visited
        visited=[0]*(k+1)
        ordering_rows=[]
        for i in range(1,k+1):
            if not dfs(i,adj_row,visited,ordering_rows): return []
        ordering_rows.reverse()

        visited=[0]*(k+1)
        ordering_cols=[]
        for i in range(1,k+1):
            if not dfs(i,adj_col, visited,ordering_cols): return []
        ordering_cols.reverse()

        row_idxs = {n:i for i,n in enumerate(ordering_rows)}
        col_idxs = {n:i for i,n in enumerate(ordering_cols)}

        ans= [[0]*k for _ in range(k)]
        for i in range(1,k+1):
            row_idx=row_idxs[i]
            col_idx=col_idxs[i]
            ans[row_idx][col_idx]=i

        return ans