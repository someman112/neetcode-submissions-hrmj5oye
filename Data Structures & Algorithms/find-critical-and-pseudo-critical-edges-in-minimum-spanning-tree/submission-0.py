class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] == -1: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px==py: return False

        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True




class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i in range(len(edges)): edges[i].append(i)
        edges.sort(key=lambda x: x[2])

        def compute_weight_ignore(ignore):
            mst_weight=0
            used_edges=0
            uf = UnionFind(n)

            for x,y,w,i in edges:
                if i!=ignore and uf.union(x,y):
                    mst_weight+=w
                    used_edges+=1
            
            if used_edges!=n-1: return float("inf")
            return mst_weight
        
        def compute_weight_force(force):
            x, y, w, i = force
            uf = UnionFind(n)
            uf.union(x, y)
            mst_weight = w
            used_edges = 1

            for x2, y2, w2, i2 in edges:
                if i2 != i and uf.union(x2, y2):
                    mst_weight += w2
                    used_edges += 1

            if used_edges != n - 1: return float("inf")
            return mst_weight

        original_weight=compute_weight_ignore(None)
        
        crit = []
        pseudo = []
        for edge in edges:
            x, y, w, i = edge
            if compute_weight_ignore(i) > original_weight:
                crit.append(i)
            elif compute_weight_force(edge) == original_weight:
                pseudo.append(i)
        
        return [crit, pseudo]