class DSU:
    
    def __init__(self, n):
        self.parent=[-1]*n
        self.rank=[-1]*n
    
    def find(self, i):
        if self.parent[i]==-1: return i
        new_parent=self.find(self.parent[i])
        self.parent[i]=new_parent
        return new_parent
            
    
    def union(self,num1,num2):
        p1,p2 = self.find(num1), self.find(num2)
        if p1==p2: return

        if self.rank[p1]>self.rank[p1]:
            self.parent[p2]=p1
        elif self.rank[p2]> self.rank[p1]:
            self.parent[p1]=p2
        else:
            self.parent[p2]=p1
            self.rank[p1]+=1
        

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                if n % d == 0:
                    factors.add(d)
                    n //= d
                else:
                    d += 1 if d == 2 else 2
            if n > 1:factors.add(n)
            return factors

        
        dsu=DSU(len(nums))
        primes_to_index={}
        for i in range(len(nums)):
            for p in prime_factors(nums[i]):
                if p not in primes_to_index:
                    primes_to_index[p]=i
                else:
                    dsu.union(i, primes_to_index[p])

        par=dsu.find(0)
        for i in range(1,len(nums)):
            if dsu.find(i)!=par: return False
        return True 
