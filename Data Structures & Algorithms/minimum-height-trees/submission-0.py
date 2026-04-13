class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges: return [0]

        adj = defaultdict(set)
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        q = deque([u for u in adj if len(adj[u])==1])

        while len(adj) > 2:
            ll = len(q)
            for _ in range(ll):
                node = q.popleft()

                for nei in adj[node]:
                    adj[nei].remove(node)
                    if len(adj[nei]) == 1: q.append(nei)
                del adj[node]
        
        return list(q)
                


